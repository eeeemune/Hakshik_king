import styled from "styled-components";
import { useTranslation } from "react-i18next";
import API from "../../../api/api";
import { useState } from "react";


const Review = () => {
    const { t } = useTranslation();
    const api = new API();
    const [review, setReview] = useState("");
    return (
        <ReviewsWrapper>
            <MenuReviewsWrapper>
                <Title>{t(`review.question_menu`)}</Title>
                <ButtonsWrapper>
                    <form method="post" action="/review_menu">
                        <Hide name="review" value={"good"}></Hide>
                        <MenuReview type="button" onClick={() => api.saveReview("review_menu", "good").then((res) => { alert('소중한 의견 감사합니다. 더 맛있는 메뉴로 찾아뵐게요!'); })}>{t(`review.good`)}</MenuReview>
                    </form>
                    <form method="post" action="/review_menu">
                        <Hide name="review" value={"bad"}></Hide>
                        <MenuReview type="button" onClick={() => api.saveReview("review_menu", "bad").then((res) => { alert('소중한 의견 감사합니다. 더 맛있는 메뉴로 찾아뵐게요!'); })} style={{ color: "#36414F", border: "1px solid #36414F" }}>{t(`review.bad`)}</MenuReview>
                    </form>
                </ButtonsWrapper>
            </MenuReviewsWrapper>
            <form method="post" action="/review">
                <HakshikkingReviewWrapper>
                    <Title>{t(`review.question_app`)}</Title>
                    <ReviewInput onChange={(e) => { setReview(e.target.value) }} value={review} className="review_form" required name="review" placeholder={t(`review.menu_placeholder`)}></ReviewInput>
                    <SubmitButton type="button" onClick={() => { review.length == 0 ? alert("내용을 입력해 주세요.") : api.saveReview("review_app", review).then((res) => { alert('소중한 의견 감사합니다. 더 좋은 학식킹으로 찾아뵐게요!'); setReview(""); }) }}>{t(`review.submit`)}</SubmitButton>
                </HakshikkingReviewWrapper>
            </form>
        </ReviewsWrapper>
    )
}


const ReviewsWrapper = styled.div`
    display:flex;
    justify-content: center;
    row-gap: 3rem;
    flex-direction: column;
    margin-top: 3rem;
`

const HakshikkingReviewWrapper = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    row-gap: 1rem;
`



const Title = styled.p`
    ${({ theme }) => theme.TEXT.default_bold};
`

const ReviewInput = styled.textarea`
    outline: none;
    border: none;
    border-radius: 1rem;
    width: 100%;
    padding: 1rem;
    box-sizing: border-box;
    min-height: 7rem;
    resize: none;
    ${({ theme }) => theme.TEXT.default};
`

const SubmitButton = styled.button`
        background-color: ${({ theme }) => theme.COLOR.orange};
    width: 100%;
    height: 3rem;
    ${({ theme }) => theme.TEXT.default_bold};
    color: white;
    border-radius: 1rem;
`

const Hide = styled.input`
    display: none;
`

const ButtonsWrapper = styled.div`
    display: flex;
    column-gap: 1rem;
    justify-content: center;
`

const MenuReview = styled.button`
    ${({ theme }) => theme.TEXT.default};
    height: 2rem;
    padding: 0 1rem;
    border-radius: 10rem;
    border: 1px solid #1563FC;
    background-color: white;
    color: #1563FC;
    line-height: 100%;
`

const MenuReviewsWrapper = styled.div`
    display: flex;
    row-gap: 1rem;
    flex-direction: column;
    text-align: center;

`

export default Review;