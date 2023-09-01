<template>
  <div class="add-book">
    <h1>Add a New Book</h1>
    <form @submit.prevent="addBook">
      <div class="form-group">
        <label for="title">Title:</label>
        <input v-model="book.title" type="text" id="title" name="title" required>
      </div>
      <div class="form-group">
        <label for="author">Author:</label>
        <input v-model="book.author" type="text" id="author" name="author" required>
      </div>
      <div class="form-group">
        <label for="year">Publication Year:</label>
        <input v-model="book.year" type="number" id="year" name="year" required>
      </div>
      <button type="submit">Add Book</button>
    </form>
  </div>
</template>

<script>
import axiosInstance from '../../axios-config.js';

export default {
  data() {
    return {
      book: {
        title: '',
        author: '',
        year: null,
      },
    };
  },
  methods: {
    async addBook() {
      try {
        const response = await axiosInstance.post('http://localhost:5002/api/add_book', this.book);
        console.log('Book added:', response.data);
        this.resetForm();
      } catch (error) {
        console.error('Error adding book:', error);
      }
    },
    resetForm() {
      this.book.title = '';
      this.book.author = '';
      this.book.year = null;
    },
  },
};
</script>


<style scoped>
.add-book {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  font-weight: bold;
}

input[type="text"],
input[type="number"] {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
