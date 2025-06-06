// let selectedCommentId = null;
// const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

// document.querySelectorAll('.delete-comment').forEach(link => {
//   link.addEventListener('click', function(e) {
//     e.preventDefault();
//     selectedCommentId = this.closest('.comment').dataset.commentId;
//     document.getElementById('passwordModal').style.display = 'block';
//   });
// });

// function closeModal() {
//   document.getElementById('passwordModal').style.display = 'none';
//   document.getElementById('commentPwInput').value = '';
// }

// document.getElementById('confirmDelete').addEventListener('click', async () => {
//   const pw = document.getElementById('commentPwInput').value;
//   if (!pw) return alert("비밀번호를 입력해주세요.");

//   if (!confirm("정말 삭제하시겠습니까?")) return;

//   const response = await fetch(`/comments/delete/${selectedCommentId}/`, {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json',
//       'X-CSRFToken': csrfToken,
//     },
//     body: JSON.stringify({ pw: pw })
//   });

//   const result = await response.json();
//   if (result.success) {
//     alert("삭제되었습니다.");
//     document.querySelector(`.comment[data-comment-id="${selectedCommentId}"]`).remove();
//   } else {
//     alert(result.message || "삭제 실패");
//   } 
//   closeModal();
// });