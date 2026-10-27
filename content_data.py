import html
E = html.escape
# ---------- shared content ----------
AREAS = [
    dict(id="general", name="General dentistry", short="Check-ups", reason="Check-up", img="svc-general",
         desc="Routine and everyday dental care for the whole family. Every plan starts here: a thorough examination of your teeth and gums, with X-rays only when they are needed.",
         list=["Dental examination", "Scaling & polishing", "Tooth extractions", "Oral & dental surgery"]),
    dict(id="preventive", name="Preventive dentistry", short="Prevention", reason="Cleaning", img="svc-gum",
         desc="Stopping dental problems before they start. Regular cleanings, sealants and fluoride, plus care for your gums, so small issues never become big ones.",
         list=["Digital X-rays", "Dental sealants", "Fluoride treatment", "Gum care (periodontics)"]),
    dict(id="restorative", name="Restorative dentistry", short="Repair", reason="Root canal", img="svc-rootcanal",
         desc="Repairing and replacing damaged or missing teeth. Implants are a focus area of Dr. Bansal, who holds a certificate in oral implantology, with consultant implantologist Dr. Sumanth S.",
         list=["Root canal treatment", "Crowns & bridges", "Composite fillings", "Inlays & onlays", "Dental implants", "Dentures"]),
    dict(id="cosmetic", name="Cosmetic dentistry", short="Smile design", reason="Smile / whitening", img="svc-cosmetic",
         desc="Smile design and aesthetic dentistry, a focus area of Dr. Bansal. Whitening is done after a check confirms your teeth and gums are healthy for it.",
         list=["Teeth whitening", "Porcelain veneers", "Smile makeover"]),
    dict(id="orthodontics", name="Orthodontics", short="Braces", reason="Braces / aligners", img="svc-braces",
         desc="Braces and clear aligners to straighten teeth and correct the bite, for teenagers and adults. After an examination we explain which option suits your teeth, budget and lifestyle.",
         list=["Traditional braces", "Clear aligners"]),
    dict(id="kids", name="Children's dentistry", short="Kids", reason="Kids", img="c19",
         desc="Gentle, unhurried visits so young patients build confidence rather than fear. Seven-day hours make it easy to come around school timings, with consultant pediatric dentist Dr. Vanessa Lobo.",
         list=["Gentle first visits", "Check-ups & cleaning", "Fluoride", "Fillings for kids"]),
]

QUOTES = [
    ("Dr. Puja is the best dentist, I'm not scared when I need to visit her! She is really friendly and nice to all patients.", "Jana Kucekova", "Czech Republic"),
    ("The clinic and facilities are good. I had a root canal and crowning and it was up to the mark, a very nice experience with a friendly doctor.", "Shirish Chavan", "Fiserv, Pune"),
    ("A very systematic doctor who is thoroughly professional and very confident with her work. Also very soft-spoken, kind, friendly and soothing, she puts all patients at ease.", "Khursheed Vakharia", "Patient"),
    ("The dental care is on a very high level. I am pleasantly surprised by the quality of work, the clinic is very clean and modern.", "Csuba Jan", "Volkswagen"),
    ("She has an amazing knowledge of patients' problems, takes care, and makes the patient comfortable while understanding the real problem.", "Rajkumar Tharmar", "HSBC, Pune"),
    ("Very nice, sweet and loving doctor. Beautiful explanations and clarifications. Excellent at dentistry. Thank you!", "Sarah Khimjee", "Patient"),
    ("The treatment was very professional and fast, and I was very happy with it. The environment is clean, and she is a very helpful and diligent dentist.", "Kollar Martin", "Volkswagen"),
    ("I found the clinic to be exactly what they promise. Dr. Puja has the experience and expertise to be one of the best.", "Mayur Naithani", "Amdocs, Pune"),
    ("It is a very soothing and satisfying experience to get treated by you. This is from all three of us. Thank you very much.", "Deepali S. Boradia", "Patient"),
    ("She was great as a dentist, useful tips to protect the enamel and avoid cavities. Makes you feel very comfortable.", "Prema Rajan", "Patient"),
    ("Awesome environment, great dentistry, graceful doctor.", "Chandra Rajan", "Foseco India"),
    ("Dear Dr. Puja, thanks a lot for your work, your patience with me and your kindness. Wish you all the best!", "Nadia Novakova", "Volkswagen"),
    ("I visited for the first time for my dental check-up. I felt satisfied with the check-up from Dr. Puja Bansal.", "Uttan Kumar Pal", "Walchand Infotech, Pune"),
    ("Very professional work, and I am absolutely content.", "Ralf Mayer", "Volkswagen"),
]
def initials(n): return "".join(w[0] for w in n.replace(".", "").split()[:2]).upper()
def vq(q, n, o): return f'<figure class="vq"><span class="stars" aria-label="Five stars">★★★★★</span><p>“{E(q)}”</p><footer><i>{initials(n)}</i><span><b>{E(n)}</b><span>{E(o)}</span></span></footer></figure>'

FAQS = {
    "visiting": ("Visiting us", [
        ("Are you accepting new patients?", "Yes, we warmly welcome new patients of all ages. Whether you are coming in for a specific treatment or just a routine check-up, we are happy to see you. Book online, call or WhatsApp +91 70287 22200, or simply visit the clinic in Viman Nagar."),
        ("What should I bring to my first appointment?", "Just yourself, a list of any medicines you take, and any previous dental X-rays or reports if you have them. If you feel nervous about dental visits, mention it when you book. Knowing helps us pace the appointment around you."),
        ("Will I see the same dentist at every visit?", "Yes. Dr. Puja Bansal (BDS) personally examines every patient and leads every treatment plan from the first visit to the final result. When a case needs specialist hands, the MDS consultant joins your treatment here in the same clinic."),
        ("Is there parking available at the clinic?", "Yes, parking is available near the DNK Square building on New Airport Road. The clinic is Office No. 503 on the 5th floor, so take the lift up. If you have trouble finding the building, call us and we will guide you in."),
        ("Is Prudent Dental Clinic good for children?", "Yes. We see children regularly and keep visits gentle, unhurried and friendly, so young patients build confidence rather than fear. Check-ups, cleaning, fluoride and fillings for kids are all available."),
    ]),
    "treatments": ("Treatments", [
        ("What dental services do you offer?", "General dentistry and check-ups, cleaning, fillings, root canal treatment, gum care, crowns, bridges and dentures, dental implants, teeth whitening and cosmetic treatments, braces and clear aligners, oral surgery and children's dentistry. Every treatment is planned by Dr. Puja Bansal after an examination."),
        ("Are dental implants available at your clinic?", "Yes. Dental implants are a focus area of Dr. Puja Bansal, who holds a certificate in oral implantology, supported by consultant periodontist and implantologist Dr. Sumanth S. Single-tooth, multiple-tooth and full-arch options are available, and every implant plan starts with an examination and imaging followed by a written, personalised quote."),
        ("Do you offer braces or clear aligners?", "Yes. We provide both traditional braces and clear aligners for teenagers and adults. After an examination, we explain which option suits your teeth, your budget and your lifestyle."),
        ("How often should I have a dental exam and cleaning?", "Most people should have their teeth examined and cleaned at least twice a year, though your dentist may recommend a different interval. Regular visits help detect cavities and gum problems early."),
    ]),
    "costs": ("Costs & safety", [
        ("How much will my treatment cost?", "There is no fixed online price, because cost depends on your diagnosis and the materials used. After an examination you get a clear, written, itemised estimate before anything starts, so you are never committed to work you have not agreed to."),
        ("Can I pay in instalments (EMI)?", "Yes. EMI is available for larger treatments such as implants, smile makeovers and braces, including no-cost EMI on eligible plans. Payment options are explained on top of your written estimate, never instead of it."),
        ("Does insurance cover dental treatment?", "Most Indian health policies exclude routine dental work; accident-related and hospitalisation cases are the usual exceptions. Some corporate and newer retail policies include dental OPD add-ons, so check your specific policy wording."),
        ("What safety and hygiene measures do you follow?", "Instruments are autoclaved, single-use items are never reused, surfaces are disinfected and barrier-covered between patients, and biomedical waste is handled properly. The clinic is deep-cleaned twice daily."),
    ]),
    "emergency": ("Emergencies", [
        ("What should I do in a dental emergency?", "Call the clinic and describe the problem rather than booking online, so you can be prioritised. We are open all 7 days, 9 AM to 9 PM (5 PM on Sundays). We are not a 24-hour clinic."),
        ("A tooth has been knocked out. What now?", "For a knocked-out adult tooth, keep it moist in milk and get to a dentist within about an hour for the best chance of saving it. Call us on the way."),
        ("When should I go to a hospital instead?", "For uncontrolled bleeding, spreading facial swelling, or trouble breathing or swallowing, go to a hospital emergency department straight away."),
    ]),
}
def qa(q, a, open_=False):
    return f'<div class="qa"><button type="button" aria-expanded="{"true" if open_ else "false"}">{E(q)}<i aria-hidden="true"></i></button><div class="qa__a"><div><p>{E(a)}</p></div></div></div>'

SPECIALISTS = [
    ("dr-godse-ai", "Dr. Mrunal Godse", "BDS, MDS (Conservative Dentistry & Endodontics)", "Consultant Endodontist", "18 years' experience", "Complex root canal treatments, re-treatments and saving heavily damaged teeth.", "Root canals"),
    ("dr-lobo-ai", "Dr. Vanessa Lobo", "BDS, MDS (Paedodontics & Preventive Dentistry)", "Consultant Pediatric Dentist", "9 years' experience, 8 as a specialist", "Gentle first visits, cavity care and prevention for infants, kids and teens.", "Kids"),
    ("dr-sumanth-ai", "Dr. Sumanth S.", "BDS, MDS (Periodontology & Oral Implantology)", "Consultant Periodontist & Implantologist", "25 years' experience, 22 as a specialist", "Advanced gum care, gum surgery and dental implant placement.", "Gums & implants"),
]

MAP_IFRAME = '<iframe title="Map to Prudent Dental Clinic, DNK Square, Viman Nagar" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q=18.5577071,73.9068639&z=16&output=embed"></iframe>'

SERVICES9 = [
    ("svc-implant", "Implant Dentistry", "Permanent replacement for missing teeth", "restorative", "Implants"),
    ("svc-general", "General Dentistry", "Routine cleanings, fillings and preventive care", "general", "Check-up"),
    ("svc-cosmetic", "Cosmetic Dentistry", "Enhance your natural smile aesthetics", "cosmetic", "Whitening"),
    ("svc-rootcanal", "Root Canal & Fillings", "Gentle treatment that saves natural teeth", "restorative", "Root canal"),
    ("svc-braces", "Braces & Aligners", "Straighten teeth with metal or clear aligners", "orthodontics", "Braces / aligners"),
    ("svc-whitening", "Teeth Whitening", "Professional brightening for a radiant smile", "cosmetic", "Whitening"),
    ("svc-smile", "Smile Designing", "Custom aesthetic restorations and veneers", "cosmetic", "Whitening"),
    ("svc-surgery", "Oral Surgery", "Safe wisdom tooth extraction and minor jaw surgery", "general", "Tooth pain"),
    ("svc-gum", "Gum Treatment", "Care for bleeding gums and periodontal problems", "preventive", "Cleaning"),
]
VIDEOS = [
    ("testimonial-implant-alex", "Alex Matthews", "On his dental implant treatment"),
    ("testimonial-root-canal", "A patient's root canal", "“It was absolutely painless”"),
    ("testimonial-implant-emi", "A patient's dental implants", "Her story, in Marathi"),
]
