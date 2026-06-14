## Changelog : maestro (30 derniers jours, au 11 juin 2026)

### Résumé
Cette période a été marquée par de nombreuses améliorations et corrections, notamment concernant la gestion des documents, des laboratoires, des prélèvements et des analyses. Des améliorations ont également été apportées à l'API et à l'intégration avec des services externes comme Brevo et S3. De nombreuses mises à jour de dépendances ont été effectuées pour maintenir la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
- Ajout de la possibilité de déposer des documents pour le suivi national [#1051](https://github.com/betagouv/maestro/issues/1051).
- Amélioration de l'affichage du tableau de bord lorsque qu'il n'y a pas d'actions prioritaires [#1054](https://github.com/betagouv/maestro/issues/1054).
- Ajout d'une API pour SEVES [#900](https://github.com/betagouv/maestro/issues/900).
- Gestion des agréments des laboratoires [#871](https://github.com/betagouv/maestro/issues/871).
- Possibilité de modifier les analytes des laboratoires en PPV [#919](https://github.com/betagouv/maestro/issues/919).
- Ajout d'une interface de configuration des laboratoires [#920](https://github.com/betagouv/maestro/issues/920).
- Amélioration du filtre sur les types de plans de programmation pour les utilisateurs [#1055](https://github.com/betagouv/maestro/issues/1055).
- Ajout du filtre par département pour les administrations centrales dans les prélèvements [#937](https://github.com/betagouv/maestro/issues/937).
- Ajout de certaines LMR optionnelles [#1013](https://github.com/betagouv/maestro/issues/1013).
- Possibilité d'imprimer le formulaire vierge pour les DAO après sélection de l'abattoir [#1011](https://github.com/betagouv/maestro/issues/1011).
- Ajout de l'identifiant de l'acteur dans Sacha [#1057](https://github.com/betagouv/maestro/issues/1057).

### Évolutions techniques
- Mise à jour de l'envoi d'emails pour utiliser le relai SMTP Brevo.
- Amélioration du typage des réponses de l'API pour une meilleure robustesse [#1006](https://github.com/betagouv/maestro/issues/1006).
- Refactorisation de l'URL pour utiliser un builder typé [#987](https://github.com/betagouv/maestro/issues/987).
- Remplacement de `swc` par `node` pour certaines tâches [#1037](https://github.com/betagouv/maestro/issues/1037).
- Correction d'un problème de capture des erreurs `console.error` avec Sentry (réversion d'un commit précédent).
- Mise à jour de plusieurs dépendances (voir section "Autres changements").

### Autres changements
- Mise à jour de nombreuses dépendances : `@aws-sdk/client-s3`, `i18next`, `storybook`, `actions/checkout`, `github/codeql-action`, `date-fns`, `react-dom`, `imapflow`, `nodemailer`, `@sentry/node`, `@sentry/react`, `vite`, `@types/node`, `@vitest/coverage-v8`, `fast-xml-parser`, `fast-xml-builder`, `@mui/material`, etc.
- Ajout d'une alerte Mattermost en cas d'échec d'envoi d'email via Brevo [#1056](https://github.com/betagouv/maestro/issues/1056).
- Correction de quelques balises dans Sacha [#1044](https://github.com/betagouv/maestro/issues/1044).
- Ajout d'un préfixe aux destinataires d'emails dans Sacha [#1047](https://github.com/betagouv/maestro/issues/1047).
- Ajout de la date de création des utilisateurs [#1038](https://github.com/betagouv/maestro/issues/1038).
- Correction de la gestion des statuts suite à l'analyse des échantillons [#947](https://github.com/betagouv/maestro/issues/947).
- Correction de la réinitialisation de la modale de recevabilité [#977](https://github.com/betagouv/maestro/issues/977).
- Correction de la duplication de la date du prélèvement dans la dernière étape [#979](https://github.com/betagouv/maestro/issues/979).
- Correction du parsing de la nouvelle syntaxe LMR par Inovalys [#1005](https://github.com/betagouv/maestro/issues/1005).
- Correction de la prise en compte des corrections apportées par Inovalys [#1004](https://github.com/betagouv/maestro/issues/1004).
- Correction de la recherche de la programmation associée à une matrice [#950](https://github.com/betagouv/maestro/issues/950).
- Correction du filtre sur les prélèvements exportés par année [#964](https://github.com/betagouv/maestro/issues/964).
- Correction de la conformité du prélèvement lors de la validation des échantillons [#981](https://github.com/betagouv/maestro/issues/981).
- Correction du status après analyse des échantillons [#978](https://github.com/betagouv/maestro/issues/978).
- Suppression des utilisateurs non actifs de la liste des préleveurs [#990](https://github.com/betagouv/maestro/issues/990).
- Ajout des types de ressources "réglementation" et "modèle" pour les documents [#988](https://github.com/betagouv/maestro/issues/988).
- Correction du numéro DAP et ajout du code barre échantillon pour les étiquettes [#951](https://github.com/betagouv/maestro/issues/951).
- Correction de la gestion des document_id dupliqués dans DAI [#938](https://github.com/betagouv/maestro/issues/938).
- Correction du nouveau nom de colonne dans Cereco [#918](https://github.com/betagouv/maestro/issues/918).
- Correction du coerce pour les DAI et les RAI [#948](https://github.com/betagouv/maestro/issues/948).
- Passage de GPG en mode non interactif [#939](https://github.com/betagouv/maestro/issues/939).
