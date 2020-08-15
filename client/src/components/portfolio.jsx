import React, { useState, useEffect } from 'react';
import { useHistory } from "react-router-dom";
import fetchData from "./fetchData";

const Portfolio = () => {
    const history = useHistory();

    const [cardList, setCardList] = useState([]);

    useEffect(() => {
        fetchCards();
    }, []);

    const fetchCards = async () => {
        let token = localStorage.getItem("token");
        if(token === null) {
            console.log("token required");
            alert("/auth/login");
        }
        else {
            fetchData('http://127.0.0.1:5000/portfolio/cards', {
                method: 'GET',
                headers: {"Content-Type": "application/json", "x-access-tokens": token}
            }).then(data => {
                console.log("success: ", data);

                setCardList(
                    data.cards.map((obj, i) => {
                        return (
                            <div className="col-md-4 d-flex align-items-stretch" key={i}>
                                <div className="card mb-4 box-shadow">
                                    <img className="card-img-top" src={obj.img} alt={obj.text} width="100%" height="160px" />
                                    <div className="card-body">
                                        <p className="card-text"><strong>{obj.title}</strong><br/>{obj.description}</p>
                                        {/* TODO: card footer */}
                                        {/* <div className="d-flex justify-content-between align-items-center"> */}
                                        {/* <div className="d-flex justify-content-between align-items-end">
                                            <div className="btn-group align-items-end">
                                                <button type="button" className="btn btn-sm btn-outline-secondary">View</button>
                                                <button type="button" className="btn btn-sm btn-outline-secondary">Edit</button>
                                            </div>
                                            <small className="text-muted">Footer</small>
                                        </div> */}

                                    </div>
                                </div>
                            </div>
                        );
                    })
                );

            }).catch(err => {
                console.log(err);
                alert(err);
                history.push("/auth/login");
            });

            
        }

    }

    return (
        <div className="album py-5">
            <div className="container">
                <div className="row">
                    {cardList}
                </div>
            </div>
        </div>
    )
}

export default Portfolio;