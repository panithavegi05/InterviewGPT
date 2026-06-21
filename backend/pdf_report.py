from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

def generate_pdf_report(
    filename,
    report
):

    doc = SimpleDocTemplate(
        filename
    )

    styles = (
        getSampleStyleSheet()
    )

    content = []

    content.append(
        Paragraph(
            "InterviewGPT Recruiter Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    for key, value in report.items():

        if isinstance(value, list):

            content.append(
                Paragraph(
                    f"<b>{key}</b>",
                    styles["Heading2"]
                )
            )

            for item in value:

                content.append(
                    Paragraph(
                        f"• {item}",
                        styles["Normal"]
                    )
                )

        else:

            content.append(
                Paragraph(
                    f"<b>{key}</b>: {value}",
                    styles["Normal"]
                )
            )

        content.append(
            Spacer(1, 6)
        )

    doc.build(content)

    return filename