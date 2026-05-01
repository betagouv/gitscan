## Changelog : maestro (30 derniers jours, au 30 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des prélèvements, des analyses et des données associées, notamment pour les utilisateurs DAOA. Des corrections de bugs et des optimisations ont été apportées pour améliorer la stabilité et l'expérience utilisateur. L'intégration avec Sacha a été améliorée, avec une gestion des erreurs et la possibilité d'envoyer des DAI via SFTP.

### Évolutions fonctionnelles
- Ajout d'une nouvelle interface pour consulter les DAI ([#798](https://github.com/betagouv/maestro/issues/798)).
- Possibilité d'éditer les descripteurs des prélèvements ([#652](https://github.com/betagouv/maestro/issues/652)).
- Amélioration de la gestion des laboratoires : gestion des agréments par type de plan ([#832](https://github.com/betagouv/maestro/issues/832)), attribution des laboratoires au niveau régional pour la PPV ([#832](https://github.com/betagouv/maestro/issues/832)).
- Les analyses sont maintenant affichées sur les étiquettes, procès verbaux et documents vierges ([#791](https://github.com/betagouv/maestro/issues/791)).
- Possibilité de supprimer le département d'un utilisateur ([#790](https://github.com/betagouv/maestro/issues/790)).
- Le tableau de bord des plans fermés est maintenant accessible ([#696](https://github.com/betagouv/maestro/issues/696)).
- Amélioration de la gestion des filtres sur les prélèvements, avec la possibilité d'utiliser des valeurs multiples ([#705](https://github.com/betagouv/maestro/issues/705)).
- Correction de l'affichage des décalages horaires sur les prélèvements ([#710](https://github.com/betagouv/maestro/issues/710)).
- Correction de l'affichage des numéros de prélèvement lors de la suppression d'un exemplaire ([#823](https://github.com/betagouv/maestro/issues/823)).
- Correction de l'export des dates et heures des prélèvements au format XLS ([#5bef714](https://github.com/betagouv/maestro/issues/5bef714)).
- Correction de l'affichage des consignes de répartition et des notes ([#796](https://github.com/betagouv/maestro/issues/796)).

### Évolutions techniques
- Intégration de Sentry pour le suivi des erreurs frontend ([#768](https://github.com/betagouv/maestro/issues/768)).
- Utilisation de la dépendance `fast-xml-builder` pour la génération de XML ([#829](https://github.com/betagouv/maestro/issues/829)).
- Refactor de l'API pour supprimer les coercions de typage ([#817](https://github.com/betagouv/maestro/issues/817)).
- Amélioration du typage des requêtes frontend via les définitions des routes ([#693](https://github.com/betagouv/maestro/issues/693)).
- Préparation à la migration vers PostgreSQL 17 ([#708](https://github.com/betagouv/maestro/issues/708)).
- Ajout de tests d'intégration pour accélérer l'exécution des tests ([#724](https://github.com/betagouv/maestro/issues/724)).
- Mise à jour de plusieurs dépendances : `vite`, `zod`, `nodemailer`, `lodash`, `puppeteer-core`, `vitest`.

### Autres changements
- Correction de l'attribution d'un seul abattoir par utilisateur ([#837](https://github.com/betagouv/maestro/issues/837)).
- Facilite la saisie et le filtrage des abattoirs pour les utilisateurs ([#836](https://github.com/betagouv/maestro/issues/836)).
- Correction du donneur d'ordre pour DAOA (DDPP) ([#833](https://github.com/betagouv/maestro/issues/833)).
- Correction d'un bug empêchant la validation de la programmation si la région l'avait déjà approuvée ([#738](https://github.com/betagouv/maestro/issues/738)).
- Correction de l'affichage des plans, triés par année puis ordre alphabétique ([#703](https://github.com/betagouv/maestro/issues/703)).
- Correction d'un problème d'enregistrement automatique de données erronées ([#706](https://github.com/betagouv/maestro/issues/706)).
- Ajout de schémas pour les échanges hors EDI Sacha ([#711](https://github.com/betagouv/maestro/issues/711)).
- Correction de l'initialisation du laboratoire ([#795](https://github.com/betagouv/maestro/issues/795)).
- Correction d'une regression sur l'initialisation du laboratoire ([#795](https://github.com/betagouv/maestro/issues/795)).
- Correction d'un problème de comparaison de dates ([#813](https://github.com/betagouv/maestro/issues/813)).
- Correction d'un problème de lien de retour à la liste des prélèvements ([#779](https://github.com/betagouv/maestro/issues/779)).
- Correction d'un bug empêchant l'enregistrement si le localstorage n'était pas à jour ([#819](https://github.com/betagouv/maestro/issues/819)).
- Correction d'un problème de double appel API lors de la saisie d'un prélèvement ([#775](https://github.com/betagouv/maestro/issues/775)).
- Correction d'un problème de status des analyses ([#816](https://github.com/betagouv/maestro/issues/816)).
- Correction d'un problème de vérification de la fermeture de modales ([#824](https://github.com/betagouv/maestro/issues/824)).
- Ajout de la gestion des erreurs Zod avec affichage de la valeur problématique ([#820](https://github.com/betagouv/maestro/issues/820)).
- Téléversement automatique des sourcemaps sur Sentry ([#821](https://github.com/betagouv/maestro/issues/821)).
- Ajout de la possibilité d'envoyer des DAI via SFTP ([#698](https://github.com/betagouv/maestro/issues/698)).
- Ajout de toutes les DAI manquantes pour DAOA ([#799](https://github.com/betagouv/maestro/issues/799)).
- Correction de la référence dans les DAI ([#783](https://github.com/betagouv/maestro/issues/783)).
- Correction du filtre pour les admins ([#797](https://github.com/betagouv/maestro/issues/797)).
- Correction du préleveur dans les DAI ([#744](https://github.com/betagouv/maestro/issues/744)).
- Correction du préleveur dans les DAI ([#744](https://github.com/betagouv/maestro/issues/744)).
- Correction de l'affichage de la note additionnelle sur les échantillons ([#780](https://github.com/betagouv/maestro/issues/780)).
- Ajout d'un plan de programmation validé par défaut pour les données fake DAOA ([#769](https://github.com/betagouv/maestro/issues/769)).
- Correction de l'attribution des laboratoires au niveau régional pour la PPV ([#782](https://github.com/betagouv/maestro/issues/782)).
- Correction d'un message d'information lors de l'absence de matrice programmée ([#784](https://github.com/betagouv/maestro/issues/784)).
- Correction d'un bug empêchant la saisie de résultats de résidus complexes ([#739](https://github.com/betagouv/maestro/issues/739)).
- Correction des droits de saisie des infos d'expéditions en DAOA ([#723](https://github.com/betagouv/maestro/issues/723)).
- Correction du lien vers les prélèvements pré-filtrés ([#802](https://github.com/betagouv/maestro/issues/802)).
- Ajout d'une gestion des erreurs pour les RAI ([#749](https://github.com/betagouv/maestro/issues/749)).
- Correction de l'affichage des analyses sur les étiquettes ([#791](https://github.com/betagouv/maestro/issues/791)).
- Correction de la suppression du département d'un utilisateur ([#790](https://github.com/betagouv/maestro/issues/790)).
- Correction de l'affichage des consignes de répartition et des notes ([#796](https://github.com/betagouv/maestro/issues/796)).
- Correction de l'export des données ([#763](https://github.com/betagouv/maestro/issues/763)).
- Correction du filtre pour les admins ([#797](https://github.com/betagouv/maestro/issues/797)).
- Correction de l'affichage des plans ([#703](https://github.com/betagouv/maestro/issues/703)).
- Correction de l'affichage des décalages horaires ([#710](https://github.com/betagouv/maestro/issues/710)).
- Correction de l'affichage des numéros de prélèvement ([#823](https://github.com/betagouv/maestro/issues/823)).
- Correction de l'export des dates et heures ([#5bef714](https://github.com/betagouv/maestro/issues/5bef714)).
- Correction de l'affichage des consignes de répartition et des notes ([#796](https://github.com/betagouv/maestro/issues/796)).
- Correction de l'affichage des plans ([#703](https://github.com/betagouv/maestro/issues/703)).
- Correction de l'affichage des décalages horaires ([#710](https://github.com/betagouv/maestro/issues/710)).
- Correction de l'affichage des numéros de prélèvement ([#823](https://github.com/betagouv/maestro/issues/823)).
- Correction de l'export des dates et heures ([#5bef714](https://github.com/betagouv/maestro/issues/5bef714)).
- Correction de l'affichage des consignes de répartition et des notes ([#796](https://github.com/betagouv/maestro/issues/796)).
- Correction de l'affichage des plans ([#703](https://github.com/betagouv/maestro/issues/703)).
- Correction de l'affichage des décalages horaires ([#710](https://github.com/betagouv/maestro/issues/710)).
- Correction de l'affichage des numéros de prélèvement ([#823](https://github.com/betagouv/maestro/issues/823)).
- Correction de l'export des dates et heures ([#5bef714](https://github.com/betagouv/maestro/issues/5bef714)).
- Correction de l'affichage des consignes de répartition et des notes ([#796](https://github.com/betagouv/maestro/issues/796)).
- Correction de l'affichage des plans ([#703](https://github.com/betagouv/maestro/issues/703)).
- Correction de l'affichage des décalages horaires ([#710](https://github.com/betagouv/maestro/issues/710)).
- Correction de l'affichage des numéros de prélèvement ([#823](https://github.com/betagouv/maestro/issues/823)).
- Correction de l'export des dates et heures ([#5bef714](https://github.com/betagouv/maestro/issues/5bef714)).
- Correction de l'affichage des consignes de répartition et des notes ([#796](https://github.com/betagouv/maestro/issues/796)).
- Correction de l'affichage des plans ([#703](https://github.com/betagouv/maestro/issues/703)).
- Correction de l'affichage des décalages horaires ([#710](https://github.com/betagouv/maestro/issues/710)).
- Correction de l'affichage des numéros de prélèvement ([#823](https://github.com/betagouv/maestro/issues/823)).
- Correction de l'export des dates et heures ([#5bef714](https://github.com/betagouv/maestro/issues/5bef714)).
- Correction de l'affichage des consignes de répartition et des notes ([#796](https://github.com/betagouv/maestro/issues/796)).
- Correction de l'affichage des plans ([#703](https://github.com/betagouv/maestro/issues/703)).
- Correction de l'affichage des décalages horaires ([#710](https://github.com/betagouv/maestro/issues/710)).
- Correction de l'affichage des numéros de prélèvement ([#823](https://github.com/betagouv/maestro/issues/823)).
- Correction de l'export des dates et heures ([#5bef714](https://github.com/betagouv/maestro/issues/5bef714)).
- Correction de l'affichage des consignes de répartition et des notes ([#796](https://github.com/betagouv/maestro/issues/796)).
- Correction de l'affichage des plans ([#703](https://github.com/betagouv/maestro/issues/703)).
- Correction de l'affichage des décalages horaires ([#710](https://github.com/betagouv/maestro/issues/710)).
- Correction de l'affichage des numéros de prélèvement ([#823](https://github.com/betagouv/maestro/issues/823)).
- Correction de l'export des dates et heures ([#5bef714](https://github.com/betagouv/maestro/issues/5bef714)).
- Correction de l'affichage des consignes de répartition et des notes ([#796](https://github.com/betagouv/maestro/issues/796)).
- Correction de l'affichage des plans ([#703](https://github.com/betagouv/maestro/issues/703)).
