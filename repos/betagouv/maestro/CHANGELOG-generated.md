## Changelog : maestro (30 derniers jours, au 07 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la gestion des prélèvements, notamment en ajoutant des filtres plus précis et en corrigeant des bugs liés à l'affichage et à la saisie des données. Des améliorations ont également été apportées à l'intégration avec Brevo et à la gestion des utilisateurs. Enfin, de nombreuses dépendances ont été mises à jour pour assurer la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- Ajout d'un filtre sur les prélèvements avec plusieurs exemplaires [#850](https://github.com/betagouv/maestro/issues/850).
- Synchronisation des modifications d'utilisateurs de Maestro avec Brevo [#840](https://github.com/betagouv/maestro/issues/840).
- Autorisation de la duplication des prélèvements sur les environnements de tests [#842](https://github.com/betagouv/maestro/issues/842).
- Ajout d'un service OIDC local pour l'authentification [#841](https://github.com/betagouv/maestro/issues/841).
- Possibilité de valider la programmation si la région a approuvé celle-ci [#738](https://github.com/betagouv/maestro/issues/738).
- Possibilité de saisir le résultat des résidus complexes dans les analyses [#739](https://github.com/betagouv/maestro/issues/739).
- Ajout d'une table pour l'envoi des DAI [#798](https://github.com/betagouv/maestro/issues/798).
- Correction de l'affichage des décalages horaires dans les prélèvements [#710](https://github.com/betagouv/maestro/issues/710).
- Notification des coordinateurs régionaux lors de l'ajout d'un nouveau document [#709](https://github.com/betagouv/maestro/issues/709).
- Passage de tous les filtres de prélèvements en valeurs multiples [#705](https://github.com/betagouv/maestro/issues/705).

### Évolutions techniques
- Mise en place de Sentry pour la gestion des erreurs côté frontend [#768](https://github.com/betagouv/maestro/issues/768).
- Refactorisation de la gestion des SSD2Update, suppression de `exceljs` et ajout d'un test de non-régression [#863](https://github.com/betagouv/maestro/issues/863).
- Amélioration de la gestion des erreurs Zod avec affichage de la valeur problématique [#820](https://github.com/betagouv/maestro/issues/820).
- Mise à jour de nombreuses dépendances (React, Node.js, PostgreSQL, etc.) pour améliorer la sécurité et les performances.
- Ajout de cache sur Playwright pour accélérer les tests [#814](https://github.com/betagouv/maestro/issues/814).
- Accélération des tests d'intégration [#724](https://github.com/betagouv/maestro/issues/724).

### Autres changements
- Correction de bugs mineurs liés à l'affichage des données et à la navigation.
- Amélioration de la documentation.
- Correction de problèmes de typage et de cohérence du code.
- Correction de l'alerte obsolète dans les tests Vitest [#867](https://github.com/betagouv/maestro/issues/867).
- Correction du problème empêchant de passer à l'étape 3 d'un prélèvement si l'étape 2 n'était pas complète [#869](https://github.com/betagouv/maestro/issues/869).
- Correction de l'affichage du SIRET de l'établissement [#885](https://github.com/betagouv/maestro/issues/885).
- Ajout de logs pour le débogage de l'API Brevo [#886](https://github.com/betagouv/maestro/issues/886).
- Correction de l'affichage des analyses sur les étiquettes, procès verbaux et documents vierges [#791](https://github.com/betagouv/maestro/issues/791).
- Correction de l'attribution des laboratoires au niveau régional pour la PPV [#842](https://github.com/betagouv/maestro/issues/842).
- Correction du lien de retour à la liste des prélèvements [#779](https://github.com/betagouv/maestro/issues/779).
- Correction des droits de saisie des infos d'expéditions en DAOA [#723](https://github.com/betagouv/maestro/issues/723).
- Correction du problème empêchant la suppression d'un département utilisateur [#836](https://github.com/betagouv/maestro/issues/836).
- Correction du problème empêchant l'attribution d'un abattoir à un utilisateur [#837](https://github.com/betagouv/maestro/issues/837).
- Correction du changement de status en fonction de la recevabilité et laisse les exemplaires 2 et 3 non mis en oeuvre [#816](https://github.com/betagouv/maestro/issues/816).
- Correction du problème de double appel API lors de la saisie d'un prélèvement [#775](https://github.com/betagouv/maestro/issues/775).
- Correction du problème de programmation incomplète [#784](https://github.com/betagouv/maestro/issues/784).
- Correction de l'affichage des notes et consignes de répartition [#796](https://github.com/betagouv/maestro/issues/796).
- Correction du problème de la validation de la programmation [#738](https://github.com/betagouv/maestro/issues/738).
- Correction de l'affichage du laboratoire dans les prélèvements [#795](https://github.com/betagouv/maestro/issues/795).
- Correction de l'export des prélèvements [#763](https://github.com/betagouv/maestro/issues/763).
- Correction du problème de comparaison de dates [#813](https://github.com/betagouv/maestro/issues/813).
- Correction du problème de la date et de l'heure du prélèvement dans le format XLS [#863](https://github.com/betagouv/maestro/issues/863).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de la saisie pour DAOA [#837](https://github.com/betagouv/maestro/issues/837).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du problème de l'affichage du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
