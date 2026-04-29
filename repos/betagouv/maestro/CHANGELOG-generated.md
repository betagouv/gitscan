## Changelog : maestro (30 derniers jours, au 28 avril 2026)

### Résumé
Ce changelog présente les améliorations apportées à Maestro au cours des 30 derniers jours. Les principales évolutions concernent l'interface de consultation des DAI, la gestion des prélèvements (notamment l'affichage des informations et la correction de bugs), ainsi que des corrections et améliorations techniques pour une meilleure stabilité et performance de l'application.

### Évolutions fonctionnelles
- Ajout d'une nouvelle interface pour consulter les DAI ([#798](https://github.com/betagouv/maestro/issues/798)).
- Amélioration de l'affichage des informations sur les prélèvements : affichage des notes additionnelles sur les échantillons, correction de l'affichage des décalages horaires ([#710](https://github.com/betagouv/maestro/issues/710)), affichage des analyses sur les étiquettes et documents.
- Possibilité d'éditer les descripteurs de prélèvements ([#652](https://github.com/betagouv/maestro/issues/652)).
- Amélioration du tableau de bord : consultation du tableau de bord des plans fermés ([#696](https://github.com/betagouv/maestro/issues/696)).
- Correction de l'affichage des liens vers les prélèvements pré-filtrés sur le dashboard ([#802](https://github.com/betagouv/maestro/issues/802)).
- Possibilité de supprimer le département d'un utilisateur ([#790](https://github.com/betagouv/maestro/issues/790)).
- Correction de l'affichage des plans de programmation, triés par année puis ordre alphabétique ([#703](https://github.com/betagouv/maestro/issues/703)).
- Correction de l'attribution des laboratoires au niveau régional pour la PPV ([#782](https://github.com/betagouv/maestro/issues/782)).

### Évolutions techniques
- Mise en place de Sentry pour la gestion des erreurs sur le frontend ([#768](https://github.com/betagouv/maestro/issues/768)).
- Refactor de l'API pour supprimer les coercions de typage trop laxistes ([#817](https://github.com/betagouv/maestro/issues/817)).
- Ajout de tests pour accélérer l'exécution des tests d'intégration ([#724](https://github.com/betagouv/maestro/issues/724)).
- Préparation de la migration vers PostgreSQL 17 ([#708](https://github.com/betagouv/maestro/issues/708)).
- Amélioration du typage des requêtes frontend via les définitions des routes dans `shared` ([#693](https://github.com/betagouv/maestro/issues/693)).
- Attente de la fin du traitement DAI avant de relancer une DAI ([#818](https://github.com/betagouv/maestro/issues/818)).
- Correction de la comparaison de dates ([#813](https://github.com/betagouv/maestro/issues/813)).
- Correction de l'erreur liée au localstorage non synchronisé avec le schéma ([#819](https://github.com/betagouv/maestro/issues/819)).
- Mise en place de l'upload automatique des sourcemaps sur Sentry ([#821](https://github.com/betagouv/maestro/issues/821)).

### Autres changements
- Ajout de schémas pour les échanges hors EDI Sacha ([#711](https://github.com/betagouv/maestro/issues/711)).
- Correction de la référence dans les DAI ([#783](https://github.com/betagouv/maestro/issues/783)).
- Correction de bugs mineurs et améliorations diverses de l'interface utilisateur.
- Mises à jour de nombreuses dépendances (nodemailer, handlebars, sass, etc.).
- Amélioration du pipeline CI/CD pour garantir la qualité du code et faciliter les déploiements ([#822](https://github.com/betagouv/maestro/issues/822), [#814](https://github.com/betagouv/maestro/issues/814)).
- Correction du numéro de prélèvement lors de la suppression d'un exemplaire ([#823](https://github.com/betagouv/maestro/issues/823)).
- Correction du status des analyses en fonction de la recevabilité ([#816](https://github.com/betagouv/maestro/issues/816)).
- Correction du filtre par entreprise ([#755](https://github.com/betagouv/maestro/issues/755)).
- Ajout d'une année et d'un ou plusieurs plans aux ressources ([#671](https://github.com/betagouv/maestro/issues/671)).
- Correction de l'affichage des consignes de répartition et des notes ([#796](https://github.com/betagouv/maestro/issues/796)).
- Correction de la regression sur l'initialisation du laboratoire ([#795](https://github.com/betagouv/maestro/issues/795)).
- Ajout d'une table pour l'envoi des DAI ([#789](https://github.com/betagouv/maestro/issues/789)).
- Masquage de l'impression des étiquettes en l'absence de type de plan ([#797](https://github.com/betagouv/maestro/issues/797)).
- Ajout de toutes les DAI manquantes pour DAOA ([#799](https://github.com/betagouv/maestro/issues/799)).
- Correction de l'affichage de la note additionnelle sur les échantillons dans le suivi du prélèvement ([#780](https://github.com/betagouv/maestro/issues/780)).
- Correction du lien de retour à la liste des prélèvements ([#779](https://github.com/betagouv/maestro/issues/779)).
- Prévention du double appel API lors de la saisie d'un prélèvement ([#775](https://github.com/betagouv/maestro/issues/775)).
- Ajout d'un plan de programmation validé par défaut pour les données fake DAOA ([#769](https://github.com/betagouv/maestro/issues/769)).
- Correction du filtre pour les admins ([#697](https://github.com/betagouv/maestro/issues/697)).
- Correction de la récupération de l'utilisateur dans le local storage ([#774](https://github.com/betagouv/maestro/issues/774)).
- Correction du champ Saisie pour DAOA.
- Correction du nom du fichier et de l'extension des DAI ([#715](https://github.com/betagouv/maestro/issues/715)).
- Déblocage des DAI pour les LNR ([#714](https://github.com/betagouv/maestro/issues/714)).
- Correction du statut des permissions ([#722](https://github.com/betagouv/maestro/issues/722)).
- Correction des droits de saisie des infos d'expéditions en DAOA ([#723](https://github.com/betagouv/maestro/issues/723)).
- Correction des notifications aux coordinateurs régionaux ([#709](https://github.com/betagouv/maestro/issues/709)).
- Correction de l'affichage des matrices réalisées ([#700](https://github.com/betagouv/maestro/issues/700)).
