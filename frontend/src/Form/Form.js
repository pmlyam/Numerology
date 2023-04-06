import React, { useEffect, useState } from "react";
import "./Form.css";
import { useForm } from "react-hook-form";

export function Form({ isSubmit, initialInfo }) {
  const [info, setInfo] = useState({
    surname: "",
    name: "",
    stepName: "",
    dateBirth: "",
  });

  const {
    register,
    handleSubmit,
    formState: { isValid, errors },
  } = useForm({
    mode: "onChange",
  });

  useEffect(() => {
    setInfo(initialInfo);
  }, [initialInfo]);

  const onSubmit = (data) => isValid && isSubmit(data);

  return (
    <section className="form" id="form">
      <div className="form__heading">
        <h2 className="form__title">
          Чтобы выполнить расшифровку, введите данные
        </h2>
        <div className="form__info">
          <span className="form__question">
            <div className="form__triangle"></div>
            <div className="form__addition">
              <p className="form__text">
                <span>Если вы изменили фамилию</span> (например в браке)
                обязательно используйте ту, что была дана при рождении
              </p>
            </div>
          </span>

          <p className="form__subtitle">Как правильно внести данные?</p>
        </div>
      </div>

      <form onSubmit={handleSubmit(onSubmit)} className="form__form">
        <label className="form__label">
          <input
            type="text"
            defaultValue={info.surname}
            {...register("surname", {
              // required: "Это поле обязательное",
              minLength: { value: 3, message: "Минимум 3 символа" },
              pattern: {
                value: /^[A-Za-zА-Яа-я]+$/,
                message: "Допускаются только буквы",
              },
            })}
            placeholder="Фамилия"
            className={`form__input ${errors.surname && "form__input_error"}`}
          />
          {errors.surname && (
            <span className="form__input-error">{errors.surname.message}</span>
          )}
        </label>

        <label className="form__label">
          <input
            type="text"
            defaultValue={info.name}
            {...register("name", {
              // required: "Это поле обязательное",
              minLength: { value: 2, message: "Минимум 2 символа" },
              pattern: {
                value: /^[A-Za-zА-Яа-я]+$/,
                message: "Допускаются только буквы",
              },
            })}
            placeholder="Имя"
            className={`form__input ${errors.name && "form__input_error"}`}
          />
          {errors.name && (
            <span className="form__input-error">{errors.name.message}</span>
          )}
        </label>

        <label className="form__label">
          <input
            type="text"
            defaultValue={info.stepName}
            {...register("stepName", {
              // required: "Это поле обязательное",
              minLength: { value: 2, message: "Минимум 2 символа" },
              pattern: {
                value: /^[A-Za-zА-Яа-я]+$/,
                message: "Допускаются только буквы",
              },
            })}
            placeholder="Отчество"
            className={`form__input ${errors.stepName && "form__input_error"}`}
          />
          {errors.stepName && (
            <span className="form__input-error">{errors.stepName.message}</span>
          )}
        </label>

        <label className="form__label">
          <input
            type="date"
            defaultValue={info.dateBirth?.split("T")[0]}
            {...register("dateBirth", {
              required: "Это поле обязательное",
              validate: {
                lessThanCurrentYear: (v) =>
                  `${new Date().getFullYear()}` !== v.split("-")[0] ||
                  "Выберите другую дату",
              },
            })}
            className={`form__input ${errors.dateBirth && "form__input_error"}`}
          />
          {errors.dateBirth && (
            <span className="form__input-error">
              {errors.dateBirth.message}
            </span>
          )}
        </label>

        <button type="submit" className="form__submit" disabled={!isValid}>
          Рассчитать
        </button>
      </form>
    </section>
  );
}
