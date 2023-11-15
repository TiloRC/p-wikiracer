import './components.css'

function FormGroup() {
  return  (
    <div class="form-group">
        <div class="start-field">
            <input type="text" name = "start"/>
        </div>
        <div class="end-field">
            <input type="text" name = "end"/>
        </div>
    </div>
  );
}

export default FormGroup;