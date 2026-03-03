## Changelog : complements-alimentaires (30 derniers jours)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'accessibilité du site, la correction de bugs et la mise à jour des dépendances. Des améliorations ont été apportées à la gestion des entreprises mandatées et à la validation des attestations d'articles 15. Des mises à jour de sécurité et de performance ont également été intégrées.

### Évolutions fonctionnelles
- Ajout de la possibilité de modifier les déclarations sans entreprises mandatées. [#2734](https://github.com/betagouv/complements-alimentaires/pull/2734)
- Amélioration de la validation automatique des articles 15, réduisant le temps d'attente.
- Ajout de l'entreprise mandatée lors de la duplication d'une déclaration.
- Mise à jour de l'entête des certificats.
- Ajout de la prise en charge de la validation du type MIME des pièces jointes des déclarations. [#2702](https://github.com/betagouv/complements-alimentaires/pull/2702)
- Amélioration de l'accessibilité des formulaires avec l'ajout d'autocomplétion pour les champs d'email et l'utilisation de switchs pour les checkboxes.
- Correction de problèmes d'accessibilité liés aux labels et aux champs de formulaire.
- Amélioration de l'ordre de tabulation des champs de formulaire.
- Ajout du logo de la MAS à l'application. [#2686](https://github.com/betagouv/complements-alimentaires/pull/2686)

### Évolutions techniques
- Mise à jour de Django en version 6.0.2. [#2706](https://github.com/betagouv/complements-alimentaires/pull/2706)
- Mise à jour de plusieurs dépendances npm et pip (vue, vue-router, core-js, etc.) pour bénéficier des dernières corrections et améliorations.
- Ajout de Metabase aux Content Security Policy (CSP). [#2700](https://github.com/betagouv/complements-alimentaires/pull/2700)
- Mise à jour de la base de données PostgreSQL dans les workflows GitHub pour une meilleure stabilité. [#2736](https://github.com/betagouv/complements-alimentaires/pull/2736)
- Suppression de l'ANR. [#2689](https://github.com/betagouv/complements-alimentaires/pull/2689)

### Autres changements
- Corrections de bugs et améliorations de l'interface utilisateur liées aux RGAA (Référentiel Général d'Accessibilité des Administrations).
- Suppression de code obsolète et nettoyage du code.
- Amélioration de la documentation et des tests.
- Correction de problèmes liés à l'affichage des erreurs de validation des fichiers.
- Correction d'un problème de retour en arrière des erreurs de validation de fichiers.
- Ajout d'un doctype dans le template de base pour permettre la génération de nonce.
- Suppression de fieldsets pour améliorer l'accessibilité.
- Correction de l'utilisation de l'attribut autocomplete.
- Amélioration de l'accessibilité des tables.
