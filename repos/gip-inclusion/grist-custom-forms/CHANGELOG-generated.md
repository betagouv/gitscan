## Changelog : grist-custom-forms (30 derniers jours, au 01 juillet 2026)

### Résumé
Les dernières mises à jour se concentrent principalement sur l'amélioration et l'extension des formulaires EURES (portail européen de la mobilité professionnelle). Cela inclut des ajustements de scoring, l'ajout de nouvelles fonctionnalités comme la transparence du matching, la personnalisation des invitations et l'intégration de champs relatifs aux conditions de travail et aux permis. Des corrections de bugs ont également été apportées pour assurer la persistance des données et le bon fonctionnement des emails.

### Évolutions fonctionnelles
- Amélioration du scoring du matching EURES.
- Ajout d'une page de transparence du matching EURES pour le public. [#1]
- Personnalisation des invitations aux candidats EURES en fonction des offres d'emploi ciblées. [#2]
- Affichage de l'offre d'emploi sélectionnée dans les emails de candidature EURES (fallback).
- Ajout de champs relatifs aux conditions de travail et aux permis dans les formulaires EURES (version bêta). [#3]
- Correction de la persistance du résumé linguistique dans les formulaires EURES. [#4]
- Le formulaire FAGERH est désormais en lecture seule. [#5]
- Renommage des libellés relatifs à la production industrielle. [#6]

### Évolutions techniques
- Refactorisation des emails d'invitation des candidats EURES pour une meilleure maintenabilité.
- Correction de la sérialisation de l'offre d'emploi cible dans les invitations EURES.
- Assouplissement des conditions de correspondance pour le travail partiel.
- Préservation des valeurs de disponibilité des contrats uniques.

### Autres changements
- Ajout de la marque EURES sur les pages du portail.
- Ajout du secteur d'activité "production industrielle" aux formulaires EURES.
- Amélioration de la formulation des emails aux candidats EURES.
