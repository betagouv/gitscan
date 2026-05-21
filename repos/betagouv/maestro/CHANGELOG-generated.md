## Changelog : maestro (30 derniers jours, au 2026-05-20)

### Résumé
Cette période a été marquée par une amélioration continue de la plateforme Maestro, avec des corrections de bugs, des améliorations de l'interface utilisateur et de nouvelles fonctionnalités, notamment autour de la gestion des prélèvements, des analyses (DAI/RAI) et de l'intégration avec des services externes comme Brevo et S3. Des efforts importants ont également été consacrés à la mise à jour des dépendances et à l'amélioration de la sécurité.

### Évolutions fonctionnelles
- Ajout d'une interface administrateur pour consulter toutes les RAI [#898](https://github.com/betagouv/maestro/issues/898).
- Ajout d'une interface de configuration des laboratoires [#920](https://github.com/betagouv/maestro/issues/920).
- Synchronisation des modifications d'utilisateurs de Maestro avec Brevo [#840](https://github.com/betagouv/maestro/issues/840).
- Possibilité de dupliquer les prélèvements sur les environnements de tests [#842](https://github.com/betagouv/maestro/issues/842).
- Amélioration de l'affichage des prélèvements pour les administrateurs [#897](https://github.com/betagouv/maestro/issues/897).
- Ajout d'une table pour stocker toutes les DAI reçues [#870](https://github.com/betagouv/maestro/issues/870).
- Ajout d'une interface au S3 local [#889](https://github.com/betagouv/maestro/issues/889).
- Amélioration de la gestion des étiquettes, affichage des analyses et suppression de restrictions [#791](https://github.com/betagouv/maestro/issues/791), [#797](https://github.com/betagouv/maestro/issues/797).
- Possibilité d'envoyer des DAI via SFTP [#698](https://github.com/betagouv/maestro/issues/698).
- Amélioration du filtre sur les prélèvements avec plusieurs exemplaires [#850](https://github.com/betagouv/maestro/issues/850).

### Évolutions techniques
- Mise à jour de nombreuses dépendances (React, TypeScript, Vite, Sentry, etc.) pour bénéficier des dernières corrections de bugs et améliorations de sécurité.
- Refactor de la gestion des erreurs Zod avec affichage de la valeur problématique [#820](https://github.com/betagouv/maestro/issues/820).
- Suppression des coerces inutiles dans l'API pour un typage plus strict [#817](https://github.com/betagouv/maestro/issues/817).
- Ajout d'un service OIDC local [#841](https://github.com/betagouv/maestro/issues/841).
- Amélioration de la gestion des sourcemaps pour Sentry [#821](https://github.com/betagouv/maestro/issues/821).
- Correction de l'alerte obsolète concernant le setup de Vitest [#867](https://github.com/betagouv/maestro/issues/867).
- Utilisation de `fast-xml-builder` pour la génération de XML [#829](https://github.com/betagouv/maestro/issues/829).

### Autres changements
- Corrections de bugs mineurs concernant l'affichage des dates, des identifiants Brevo, des numéros de prélèvements et des informations sur les laboratoires.
- Amélioration des logs pour faciliter le débogage de l'API Brevo [#886](https://github.com/betagouv/maestro/issues/886).
- Amélioration de la gestion des erreurs et des validations dans les formulaires.
- Diverses corrections et améliorations de la CI/CD.
- Mise à jour de la documentation.
- Nettoyage du code et refactoring de certains composants.
- Correction de la référence dans les DAI [#883](https://github.com/betagouv/maestro/issues/883).
- Correction des dates dans les exports DAI.
- Correction de la comparaison de dates dans les prélèvements [#779](https://github.com/betagouv/maestro/issues/779).
- Correction de l'affichage des notes additionnelles sur les échantillons [#780](https://github.com/betagouv/maestro/issues/780).
- Correction du lien de retour à la liste des prélèvements [#775](https://github.com/betagouv/maestro/issues/775).
- Correction de l'attribution des laboratoires au niveau régional [#782](https://github.com/betagouv/maestro/issues/782).
- Correction de la suppression des abattoirs [#836](https://github.com/betagouv/maestro/issues/836).
- Correction de l'affichage des consignes de répartition et des notes [#796](https://github.com/betagouv/maestro/issues/796).
- Correction de l'affichage des étiquettes [#795](https://github.com/betagouv/maestro/issues/795).
- Correction de l'initialisation du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du double appel API lors de la saisie d'un prélèvement [#775](https://github.com/betagouv/maestro/issues/775).
- Correction de l'affichage des analyses sur les étiquettes [#791](https://github.com/betagouv/maestro/issues/791).
- Correction de la gestion des status suite à l'analyse des échantillons [#947](https://github.com/betagouv/maestro/issues/947).
- Correction des document_id dupliqués [#938](https://github.com/betagouv/maestro/issues/938).
- Correction de l'extraction du numéro d'exemplaire [#937](https://github.com/betagouv/maestro/issues/937).
- Correction de la gestion des non quantifiables dans Cereco [#945](https://github.com/betagouv/maestro/issues/945).
- Ajout du coerce pour les DAI et les RAI [#948](https://github.com/betagouv/maestro/issues/948).
- Application de Zod à toutes les réponses de l'API [#946](https://github.com/betagouv/maestro/issues/946).
- Correction de l'affichage des prélèvements pour les admins [#897](https://github.com/betagouv/maestro/issues/897).
- Correction du problème empêchant de passer à la 3ème étape du prélèvement si la 2ème n'est pas chargée [#869](https://github.com/betagouv/maestro/issues/869).
- Correction de l'affichage du siret de l'établissement [#885](https://github.com/betagouv/maestro/issues/885).
- Correction de la restriction à une seule attribution d'abattoir [#837](https://github.com/betagouv/maestro/issues/837).
- Correction du filtre sur les prélèvements avec plusieurs exemplaires [#850](https://github.com/betagouv/maestro/issues/850).
- Correction du message d'alerte pour la vérification des informations avant l'envoi du prélèvement [#902](https://github.com/betagouv/maestro/issues/902).
- Correction des identifiants de listes Brevo [#901](https://github.com/betagouv/maestro/issues/901).
- Correction du changement de status en fonction de la recevabilité et des exemplaires [#816](https://github.com/betagouv/maestro/issues/816).
- Correction de la gestion des consignes de répartition et des notes [#796](https://github.com/betagouv/maestro/issues/796).
- Correction de l'affichage des analyses sur les étiquettes [#791](https://github.com/betagouv/maestro/issues/791).
- Correction de l'affichage des notes additionnelles sur les échantillons [#780](https://github.com/betagouv/maestro/issues/780).
- Correction du lien de retour à la liste des prélèvements [#779](https://github.com/betagouv/maestro/issues/779).
- Correction de l'attribution des laboratoires au niveau régional [#782](https://github.com/betagouv/maestro/issues/782).
- Correction de la suppression des abattoirs [#836](https://github.com/betagouv/maestro/issues/836).
- Correction de l'affichage des consignes de répartition et des notes [#796](https://github.com/betagouv/maestro/issues/796).
- Correction de l'affichage des étiquettes [#795](https://github.com/betagouv/maestro/issues/795).
- Correction de l'initialisation du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du double appel API lors de la saisie d'un prélèvement [#775](https://github.com/betagouv/maestro/issues/775).
- Correction de l'affichage des analyses sur les étiquettes [#791](https://github.com/betagouv/maestro/issues/791).
- Correction de la gestion des status suite à l'analyse des échantillons [#947](https://github.com/betagouv/maestro/issues/947).
- Correction des document_id dupliqués [#938](https://github.com/betagouv/maestro/issues/938).
- Correction de l'extraction du numéro d'exemplaire [#937](https://github.com/betagouv/maestro/issues/937).
- Correction de la gestion des non quantifiables dans Cereco [#945](https://github.com/betagouv/maestro/issues/945).
- Ajout du coerce pour les DAI et les RAI [#948](https://github.com/betagouv/maestro/issues/948).
- Application de Zod à toutes les réponses de l'API [#946](https://github.com/betagouv/maestro/issues/946).
- Correction de l'affichage des prélèvements pour les admins [#897](https://github.com/betagouv/maestro/issues/897).
- Correction du problème empêchant de passer à la 3ème étape du prélèvement si la 2ème n'est pas chargée [#869](https://github.com/betagouv/maestro/issues/869).
- Correction de l'affichage du siret de l'établissement [#885](https://github.com/betagouv/maestro/issues/885).
- Correction de la restriction à une seule attribution d'abattoir [#837](https://github.com/betagouv/maestro/issues/837).
- Correction du filtre sur les prélèvements avec plusieurs exemplaires [#850](https://github.com/betagouv/maestro/issues/850).
- Correction du message d'alerte pour la vérification des informations avant l'envoi du prélèvement [#902](https://github.com/betagouv/maestro/issues/902).
- Correction des identifiants de listes Brevo [#901](https://github.com/betagouv/maestro/issues/901).
- Correction du changement de status en fonction de la recevabilité et des exemplaires [#816](https://github.com/betagouv/maestro/issues/816).
- Correction de la gestion des consignes de répartition et des notes [#796](https://github.com/betagouv/maestro/issues/796).
- Correction de l'affichage des analyses sur les étiquettes [#791](https://github.com/betagouv/maestro/issues/791).
- Correction de l'affichage des notes additionnelles sur les échantillons [#780](https://github.com/betagouv/maestro/issues/780).
- Correction du lien de retour à la liste des prélèvements [#779](https://github.com/betagouv/maestro/issues/779).
- Correction de l'attribution des laboratoires au niveau régional [#782](https://github.com/betagouv/maestro/issues/782).
- Correction de la suppression des abattoirs [#836](https://github.com/betagouv/maestro/issues/836).
- Correction de l'affichage des consignes de répartition et des notes [#796](https://github.com/betagouv/maestro/issues/796).
- Correction de l'affichage des étiquettes [#795](https://github.com/betagouv/maestro/issues/795).
- Correction de l'initialisation du laboratoire [#795](https://github.com/betagouv/maestro/issues/795).
- Correction du double appel API lors de la saisie d'un prélèvement [#775](https://github.com/betagouv/maestro/issues/775).
- Correction de l'affichage des analyses sur les étiquettes [#791](https://github.com/betagouv/maestro/issues/791).
- Correction de la gestion des status suite à l'analyse des échantillons [#947](https://github.com/betagouv/maestro/issues/947).
- Correction des document_id dupliqués [#938](https://github.com/betagouv/maestro/issues/938).
- Correction de l'extraction du numéro d'exemplaire [#937](https://github.com/betagouv/maestro/issues/937).
- Correction de la gestion des non quantifiables dans Cereco [#945](https://github.com/betagouv/maestro/issues/945).
- Ajout du coerce pour les DAI et les RAI [#948](https://github.com/betagouv/maestro/issues/948).
