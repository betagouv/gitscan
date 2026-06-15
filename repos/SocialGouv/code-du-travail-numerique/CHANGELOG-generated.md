## Changelog : code-du-travail-numerique (30 derniers jours, au 10 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'outil "Trouver sa CC" avec l'ajout des accords d'entreprise, ainsi que sur des corrections de bugs et des améliorations de la recherche et de la contribution. Des ajustements ont également été apportés au calcul du SMIC et à la gestion des contributions.

### Évolutions fonctionnelles
- Ajout des accords d'entreprise dans l'outil "Trouver sa CC" ([#7260](https://github.com/SocialGouv/code-du-travail-numerique/issues/7260)).
- Amélioration du support de l'inaptitude pour les assistants maternels de la convention collective 3239 ([#7276](https://github.com/SocialGouv/code-du-travail-numerique/issues/7276)).
- Ajout de méthodes de calcul sur le SMIC annuel ([#7286](https://github.com/SocialGouv/code-du-travail-numerique/issues/7286)).
- Support du challenger pour les modifications du SMIC sur les contributions ([#7284](https://github.com/SocialGouv/code-du-travail-numerique/issues/7284)).
- Correction de l'affichage de l'astérisque sur le brut dans la contribution ([#7288](https://github.com/SocialGouv/code-du-travail-numerique/issues/7288)).
- Correction d'un bug bloquant l'affichage des informations en contribution sans CC sélectionnée ([#7232](https://github.com/SocialGouv/code-du-travail-numerique/issues/7232)).

### Évolutions techniques
- Correction de problèmes HTML invalides sur la page d'accueil ([#7292](https://github.com/SocialGouv/code-du-travail-numerique/issues/7292)).
- Correction des tests unitaires suite aux modifications du 1er juin ([#7295](https://github.com/SocialGouv/code-du-travail-numerique/issues/7295)).
- Amélioration du seuil de "fuzziness" pour la recherche de définitions ([#7265](https://github.com/SocialGouv/code-du-travail-numerique/issues/7265)).
- Correction du widget de recherche qui ne s'ouvrait plus ([#7294](https://github.com/SocialGouv/code-du-travail-numerique/issues/7294)).
- Correction des "keys props" des résultats de recherche ([#7293](https://github.com/SocialGouv/code-du-travail-numerique/issues/7293)).

### Autres changements
- Mise à jour des dépendances ([#7297](https://github.com/SocialGouv/code-du-travail-numerique/issues/7297)).
- Désactivation du quizz sur la page d'accueil ([#7284](https://github.com/SocialGouv/code-du-travail-numerique/issues/7284)).
- Corrections et améliorations mineures sur la POC des accords d'entreprise ([#7306](https://github.com/SocialGouv/code-du-travail-numerique/issues/7306)).
- Correction de la valeur du SMIC mal renseignée.
- Ajout d'attributs à la "whitelist" du challenger SMIC.
