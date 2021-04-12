import React from 'react';
import ReactDOM from 'react-dom';

const App = () => {
    return (
        <div>Welcome from React</div>
    )
}

let props;
try{
    props = {...context};
}
catch(e){
    props = {}
}

ReactDOM.render(<App {...props}></App>, document.getElementById('root'));
if(module.hot) {
    module.hot.accept();
}