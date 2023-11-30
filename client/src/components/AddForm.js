import React from "react";
import { Formik, Form, Field, ErrorMessage } from "formik";

 const AddForm = () => {
    return (
      <div className="form-field">
        <h1>Add An Amenity</h1>
        <Formik 
        initialValues={{amenityname:''}}
        validate={values => {
            const errors = {};
            if (!values.amenityname) {
                errors.amenityname = 'Amenity name must be greater than 1 character';
            } 
            return errors;
        }}
        onSubmit={(values, {setSubmitting}) => {
            setTimeout(() => {
                alert(JSON.stringify(values, null, 2))
                setSubmitting(false)}, 400)
                }}>
        {({ isSubmitting }) => (
        <Form>
            <Field
            type="text"
            name="amenityname"
            placeholder="Enter the amenity" />
            <ErrorMessage name="amenityname" component="div" />
            <button type="submit" disabled={isSubmitting}>
                Submit
                </button>
        </Form>
        )}
        </Formik>
    </div>
    )
 };

export default AddForm;