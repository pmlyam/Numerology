const BASE_URL = "http://localhost/";

const handleReturn = (res) => {
  if (res.ok) {
    return res.json();
  }
  return Promise.reject(res.status);
};

// регистрация через post /signup - не реализовано
export const authRegister = (user) => {
  return fetch(`${BASE_URL}/signup`, {
    method: "POST",
    credentials: "include",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      name: user.name,
      email: user.email,
      password: user.password,
    }),
  }).then((res) => handleReturn(res));
};
// авторизация через post /signin  - не реализовано
export const authCheckIn = (user) => {
  return fetch(`${BASE_URL}/signin`, {
    method: "POST",
    credentials: "include",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email: user.email,
      password: user.password,
    }),
  }).then((res) => handleReturn(res));
};
// получение токена и данных профиля через get /users/me  - не реализовано
export const authTokenCheck = () => {
  return fetch(`${BASE_URL}/users/me`, {
    method: "GET",
    credentials: "include",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
  }).then((res) => handleReturn(res));
};
// выход из аккаунта post /signout  - не реализовано
export const authCheckOut = () => {
  return fetch(`${BASE_URL}/signout`, {
    method: "POST",
    credentials: "include",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
  });
};
// обновляет информацию о пользователе через patch /users/me  - не реализовано
export const handleEditUserInfo = (user) => {
  return fetch(`${BASE_URL}/users/me`, {
    method: "PATCH",
    credentials: "include",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      _id: user._id,
      name: user.name,
      email: user.email,
    }),
  }).then((res) => handleReturn(res));
};

// отправка даты рождения на сервер
export const handleSendingBirthDate = (data) => {
  return fetch(`/api/`, {
    // mode: "no-cors", // временная заглушка CORS
    method: "POST",
    credentials: "include",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
      Origin: "https://dimdimshishkov.github.io/Numerology/",
    },
    body: JSON.stringify({
      date: data.split("-").reverse().join("."),
    }),
  }).then((res) => handleReturn(res));
};
