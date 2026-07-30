## Changelog : data-inclusion (30 derniers jours, au 29 juillet 2026)

### Résumé
Cette mise à jour améliore la qualité et la fiabilité des données traitées par la plateforme, notamment en corrigeant des erreurs dans le pipeline de traitement et en améliorant la recherche. L'API a également été ajustée pour mieux refléter les données disponibles.

### Évolutions fonctionnelles
- Amélioration de la recherche : la recherche est désormais plus robuste face aux erreurs de frappe.
- Correction de la pondération des thématiques et des noms de structures dans l'API.
- Prise en compte de la nouvelle catégorie "cooling_space" dans le pipeline de données.
- Correction de l'affichage des services Carif-Oref pour garantir une cohérence des données.

### Évolutions techniques
- Correction de plusieurs problèmes de déterminisme dans le pipeline de traitement des données (réseau-alpha, carif-oref, les-emplois).
- Correction des types de données incorrects (âge minimum en nombre entier) dans les données MBA.
- Correction de l'émission des organismes Carif-Oref publics.
- Adaptation du pipeline pour prendre en charge le nouveau type "Orienteur" dans les données "les-emplois".
- Correction des modes de contact "courriel" pour la source "mediation-numerique".
- Modification du canal Slack utilisé pour les résumés du pipeline.

### Autres changements
Aucun changement supplémentaire à signaler.
