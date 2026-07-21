## Changelog : mon-entreprise (30 derniers jours, au 2026-07-16)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau du comparateur et des simulateurs. Des corrections ont été apportées pour affiner les calculs et l'affichage des informations, en particulier pour Mayotte et les travailleurs frontaliers suisses. Des efforts ont également été faits pour améliorer la documentation et la maintenabilité du code.

### Évolutions fonctionnelles
- Ajout du statut AE au simulateur de choix de statut.
- Amélioration de l'affichage des réponses dans le comparateur, avec une meilleure organisation et des liens vers la documentation.
- Ajout d'un avertissement pour les auto-entrepreneureuses dans le simulateur indépendant.
- Amélioration de l'avertissement du simulateur de dividendes.
- Le simulateur de cotisation maladie des travailleurs frontaliers suisses est maintenant disponible.
- Possibilité de préciser la situation des travailleurs frontaliers suisses dès que les questions principales sont répondues.
- Ajout d'un lien de partage pour le simulateur frontalier suisse.
- Correction de l'affichage des exonérations à Mayotte.
- Correction de l'arrondi des cotisations RC et ID pour les conjoints collaborateurs PLR Cipav.
- Correction de l'application de la réforme de l'acre (critère = date de création de l'entreprise).
- Correction de l'Acre non applicable en outre-mer.
- Correction de l'affichage des dates dans le simulateur frontalier suisse.
- Amélioration de l'accessibilité de certains éléments (Switch, icônes).
- Correction de la position de l'infobulle par rapport au choix de période de calcul.

### Évolutions techniques
- Refactor de la gestion des questions et des groupes de questions dans le comparateur.
- Amélioration de l'architecture du frontend avec l'ajout d'un adaptateur d'environnement portable Vite/Next.
- Suppression du client Fabrique Social inutilisé.
- Amélioration de la gestion des erreurs Redis avec l'ajout de remontées à Sentry.
- Refactor de la gestion des langues et des traductions, avec une meilleure organisation des fichiers et des constantes.
- Simplification de certains composants et suppression de code inutile.
- Amélioration de la documentation et ajout de tests unitaires.
- Mise à jour des paquets `modele-xx`.
- Correction d'un problème d'affichage sur Chrome et Edge pour les légendes des champs.

### Autres changements
- Mise à jour de la documentation sur la librairie de calcul.
- Mise à jour de la date dans le footer.
- Amélioration de la documentation du simulateur de location de meublé.
- Correction de la documentation sur le mode d'imposition de l'entreprise.
- Ajout de descriptions aux paquets `modele-as` et `modele-ti`.
- Masquage du simulateur TFS du menu et de la liste des outils.
- Correction de quelques erreurs de traduction.
- Suppression d'un appel de hook non importé dans la documentation micro-BIC.
- Correction d'un problème de formatage des dates.
- Amélioration de la lisibilité du code.
- Ajout de commentaires et de documentation.
