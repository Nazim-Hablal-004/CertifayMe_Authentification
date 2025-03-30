import React, { useState } from "react";
import axios from "axios";

const Register = () => {
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
    role: "student",
    name: "",
    address: "",
    phone: "",
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("http://localhost:8000/auth/register/", formData);
      alert(res.data.message);
    } catch (err) {
      console.error(err.response.data);
      alert("Erreur lors de l'inscription");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" name="username" onChange={handleChange} placeholder="Nom d'utilisateur" required />
      <input type="email" name="email" onChange={handleChange} placeholder="Email" required />
      <input type="password" name="password" onChange={handleChange} placeholder="Mot de passe" required />

      <select name="role" onChange={handleChange}>
        <option value="student">Étudiant</option>
        <option value="university">Université</option>
        <option value="companies">Entreprise</option>
        <option value="minister">Ministère</option>
      </select>

      <button type="submit">S'inscrire</button>
    </form>
  );
};

export default Register;
