import { defineStore } from 'pinia'
import { useUserStore } from './user'

export const useCommentsStore = defineStore({
    id: 'comments',
    state: () => ({
        comments: [
        // {
        //"id":"1",
        //"content":"bla bla bla",
        //"user_id":"45",
        //"user_name":"John Doe",        
        //"micropost_id":"105", 
        //"created_at":"2016-10-18 12:14:51",                              
        //}
        ]
    }),
    getters: {
        getComments (state) {
            return state.comments;
        },
        getPostComments: (state) => (id) => {
            const results = state.comments.filter(c => {
                return c.micropost_id == id;
              })
              return results
        },
    }, 
    actions: {

        addComments(comments) {
            this.comments = comments
        },
        addComment(comment) {
            this.comments = [...this.comments, comment]
        },

        async getCommentsDB() {
			try {
				const response = await fetch(`http://daw.deei.fct.ualg.pt/~a12345/LAB8_10/api/comments.php`)
				const data = await response.json()
                this.addComments(data)
                return true
			} 
			catch (error) {
				console.error(error)
                return false
			}
		},
        async addCommentDB(newComment) {
			try {
                const userStore = useUserStore()
				const response = await fetch(`http://daw.deei.fct.ualg.pt/~a12345/LAB8_10/api/comments.php?micropost_id=${newComment.post_id}&session_id=${userStore.user.session_id}`, {
					method: 'POST',
					body: JSON.stringify(newComment),
					headers: { 'Content-type': 'application/json; charset=UTF-8' },
				})
				const data = await response.json()
                console.log(data)
                this.addComment(data)
                return true
			} 
			catch (error) {
				console.error(error)
                return false
			}
		},

    }
})



