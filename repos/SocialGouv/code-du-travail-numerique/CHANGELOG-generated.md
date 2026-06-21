## Changelog : code-du-travail-numerique (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion des accords d'entreprise, la correction de bugs affectant la recherche et l'affichage des informations, ainsi que des ajustements pour améliorer la précision des calculs liés au SMIC. Des corrections ont également été apportées aux tests et à la gestion des redirections.

### Évolutions fonctionnelles
- Ajout de la prise en charge des accords d'entreprise dans l'outil "Trouver sa convention collective" ([#7260](https://github.com/SocialGouv/code-du-travail-numerique/issues/7260)).
- Amélioration des méthodes de calcul du SMIC annuel ([#7286](https://github.com/SocialGouv/code-du-travail-numerique/issues/7286)).
- Correction de l'affichage du code IDCC 9999 pour une meilleure normalisation ([#7303](https://github.com/SocialGouv/code-du-travail-numerique/issues/7303)).
- Les accords d'entreprise sont maintenant ordonnés par date de signature.

### Évolutions techniques
- Correction de tests unitaires suite à des modifications récentes ([#7295](https://github.com/SocialGouv/code-du-travail-numerique/issues/7295)).
- Correction de problèmes HTML invalides sur la page d'actualités.
- Correction de bugs affectant le widget de recherche et l'ouverture de la page de recherche.
- Correction de l'affichage des informations de contribution lorsque aucune convention collective n'est sélectionnée ([#7232](https://github.com/SocialGouv/code-du-travail-numerique/issues/7232)).

### Autres changements
- Correction de redirections vers la page d'information sur les canicules ([#7318](https://github.com/SocialGouv/code-du-travail-numerique/issues/7318), [#7322](https://github.com/SocialGouv/code-du-travail-numerique/issues/7322)).
- Suppression de la balise canonical redondante sur la page de contribution ([#7316](https://github.com/SocialGouv/code-du-travail-numerique/issues/7316)).
- Mise à jour des dépendances du projet ([#7297](https://github.com/SocialGouv/code-du-travail-numerique/issues/7297)).
- Correction de l'astérisque manquant sur le brut de la contribution ([#7288](https://github.com/SocialGouv/code-du-travail-numerique/issues/7288)).
- Ajout d'attributs à la whitelist du challenger SMIC pour corriger des erreurs de calcul.
- Correction de problèmes liés aux keys props des résultats de recherche ([#7293](https://github.com/SocialGouv/code-du-travail-numerique/issues/7293)).
- Correction de l'affichage des informations sur l'inaptitude pour les assistants maternels de la convention collective 3239 ([#7276](https://github.com/SocialGouv/code-du-travail-numerique/issues/7276)).
