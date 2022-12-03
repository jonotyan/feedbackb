from feedbackb.keyboards.text_templates import (feedback_template_w_u,
                                                feedback_template)


async def message_format(data, is_username):
    if is_username:
        return feedback_template.format(
            data['user_feedback_text'],
            data['first_name'],
            f'@{data["username"]}',
        )
    return feedback_template_w_u.format(
        data['user_feedback_text'],
        data['first_name']
    )


