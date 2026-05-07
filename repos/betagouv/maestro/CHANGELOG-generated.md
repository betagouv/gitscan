## Changelog : maestro (30 derniers jours, au 6 mai 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de la gestion des prélèvements et des analyses, notamment avec l'ajout de filtres plus précis, la correction de bugs liés à l'affichage et à la saisie de données, et l'amélioration de l'intégration avec des services externes comme Brevo et Sacha. Des efforts ont également été déployés pour améliorer la qualité du code, la sécurité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout d'un filtre sur les prélèvements avec plusieurs exemplaires [#850](https://github.com/betagouv/maestro/issues/850).
- Synchronisation des modifications d'utilisateurs de Maestro avec Brevo [#840](https://github.com/betagouv/maestro/issues/840).
- Possibilité de dupliquer les prélèvements sur les environnements de tests [#842](https://github.com/betagouv/maestro/issues/842).
- Affichage des analyses sur les étiquettes, procès verbaux et documents vierges [#791](https://github.com/betagouv/maestro/issues/791).
- Ajout d'une interface pour consulter les DAI [#798](https://github.com/betagouv/maestro/issues/798).
- Possibilité de valider la programmation si la région a approuvé celle-ci [#738](https://github.com/betagouv/maestro/issues/738).
- Possibilité de saisir le résultat des résidus complexes [#739](https://github.com/betagouv/maestro/issues/739).
- Ajout d'un service OIDC local [#841](https://github.com/betagouv/maestro/issues/841).
- Amélioration de l'affichage des décalages horaires [#710](https://github.com/betagouv/maestro/issues/710).
- Notification des coordinateurs régionaux lors de l'ajout d'un nouveau document [#709](https://github.com/betagouv/maestro/issues/709).
- Tri des plans par année puis ordre alphabétique [#703](https://github.com/betagouv/maestro/issues/703).
- Déblocage des DAI pour les LNR [#714](https://github.com/betagouv/maestro/issues/714).
- Possibilité de passer à la 3ème étape d'un prélèvement seulement si les éléments de la 2ème étape sont chargés [#869](https://github.com/betagouv/maestro/issues/869).

### Évolutions techniques
- Refactor de la gestion des SSD2Update, suppression de `exceljs` et ajout d'un test de non-régression [#863](https://github.com/betagouv/maestro/issues/863).
- Typage des requêtes frontend via les définitions des routes dans `shared` [#693](https://github.com/betagouv/maestro/issues/693).
- Préparation à la migration vers PostgreSQL 17 [#708](https://github.com/betagouv/maestro/issues/708).
- Utilisation de `fast-xml-builder` pour la gestion du XML [#829](https://github.com/betagouv/maestro/issues/829).
- Amélioration de la gestion des erreurs Zod avec affichage de la valeur problématique [#820](https://github.com/betagouv/maestro/issues/820).
- Ajout de l'envoi automatique des sourcemaps sur Sentry [#821](https://github.com/betagouv/maestro/issues/821).
- Suppression des coercions de type dans l'API pour un typage plus strict [#817](https://github.com/betagouv/maestro/issues/817).
- Ajout d'un cache pour Playwright (en cours d'optimisation) [#814](https://github.com/betagouv/maestro/issues/814).

### Autres changements
- Mise à jour de nombreuses dépendances (React, TypeScript, Vite, etc.). Ces mises à jour sont principalement des corrections de bugs et des améliorations de sécurité.
- Amélioration de la documentation avec l'ajout de schémas pour les échanges hors EDI Sacha [#711](https://github.com/betagouv/maestro/issues/711).
- Correction de divers bugs et améliorations de l'expérience utilisateur.
- Correction de l'alerte concernant le setup obsolète de Vitest [#867](https://github.com/betagouv/maestro/issues/867).
- Correction de l'affichage du champ "Saisie" pour DAOA.
- Correction du lien de retour à la liste des prélèvements.
- Correction de l'attribution des laboratoires au niveau régional pour la PPV.
- Correction de l'affichage des notes additionnelles sur les échantillons.
- Correction de l'affichage des étiquettes en l'absence de type de plan.
- Correction de l'initialisation du laboratoire.
- Correction de la gestion des droits de saisie des infos d'expéditions en DAOA.
- Correction de la gestion des plans de programmation validés par défaut pour les données fake DAOA.
- Correction du message d'info lors de l'absence de matrice programmée pour le plan de surveillance.
- Correction de la suppression des exemplaires de prélèvement.
- Correction de l'affichage des numéros lors de la suppression d'un exemplaire.
- Correction de l'affichage des consignes de répartition et des notes.
- Correction du problème de double appel API lors de la saisie d'un prélèvement.
- Correction du problème d'enregistrement automatique de données erronées.
- Correction du problème d'affichage des étiquettes en l'absence de type de plan.
- Correction du problème d'affichage des analyses sur les étiquettes.
- Correction de la suppression du département utilisateur.
- Correction de l'affichage du nom du fichier et de l'extension DAI.
- Correction du problème de comparaison de dates.
- Correction du problème de localstorage non synchronisé avec le schéma.
- Ajout d'un test pour vérifier que la modale n'a pas déjà été fermée.
- Correction de l'export des prélèvements.
- Correction du problème de gestion des agréments par type de plan.
- Ajout de la date et de l'heure du prélèvement dans le format XLS.
- Correction du bug empêchant l'attribution d'un abattoir qu'une seule fois.
- Correction de l'affichage du donneur d'ordre pour DAOA (DDPP).
- Ajout de la possibilité de filtrer les utilisateurs par abattoir.
- Ajout d'un message d'information si pas d'échantillon saisissable à cause d'une programmation incomplète.
- Ajout de la possibilité de synchroniser les modifications d'utilisateurs de Maestro avec Brevo.
- Ajout d'une nouvelle interface pour consulter les DAI.
- Ajout d'un filtre sur les prélèvements avec plusieurs exemplaires.
- Ajout de la possibilité de dupliquer les prélèvements sur les environnements de tests.
- Ajout de la gestion des erreurs pour les RAI.
- Ajout de la possibilité d'envoyer des DAI via SFTP.
- Ajout de la gestion des erreurs pour les RAI.
- Amélioration de la documentation.
- Diverses corrections de bugs et améliorations de la qualité du code.
