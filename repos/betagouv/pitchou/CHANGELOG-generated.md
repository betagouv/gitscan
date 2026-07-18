## Changelog : pitchou (30 derniers jours, au 17 juillet 2026)

### Résumé
Ce mois-ci, les évolutions de Pitchou se concentrent sur l'amélioration de l'expérience utilisateur pour les instructeurs et administrateurs, notamment en facilitant l'accès aux informations clés des dossiers, la gestion des pièces jointes et la synchronisation avec l'API Démarche Numérique. Des corrections ont également été apportées pour assurer la stabilité et la fiabilité de la plateforme.

### Évolutions fonctionnelles
- Les instructeurs peuvent désormais contacter le déposant du dossier directement depuis l'entête du dossier. [#630](https://github.com/betagouv/pitchou/issues/630)
- Ajout d'un onglet "Porteur de projet" pour faciliter l'accès aux informations du porteur de projet. [#627](https://github.com/betagouv/pitchou/issues/627)
- Possibilité d'afficher et de télécharger la cartographie associée à un dossier pour les instructeurs. [#629](https://github.com/betagouv/pitchou/issues/629)
- Amélioration de la réactivité de la date des prescriptions et ajout d'un rafraîchissement du dossier en cache pour les instructeurs. [#648](https://github.com/betagouv/pitchou/issues/649)
- Ajout d'une modale pour la gestion des pièces jointes dans l'interface instructeur. [#634](https://github.com/betagouv/pitchou/issues/634)
- Les dates de consultation du public et le champ "enjeux" sont désormais modifiables dans l'onglet instruction. [#600](https://github.com/betagouv/pitchou/issues/604)
- Affichage des liens des documents dans l'interface des espèces. [#635](https://github.com/betagouv/pitchou/issues/635)
- Possibilité d'accepter les fichiers .xlsx pour les espèces. [#628](https://github.com/betagouv/pitchou/issues/628)
- Ajout d'un bouton "Retour" dans l'interface instructeur. [#609](https://github.com/betagouv/pitchou/issues/609)
- Ajout d'un fil d'Ariane pour faciliter la navigation. [#610](https://github.com/betagouv/pitchou/issues/610)
- Ajout de domaines PACA et ext.beta.gouv.fr autorisés pour l'authentification. [#641](https://github.com/betagouv/pitchou/issues/641), [#601](https://github.com/betagouv/pitchou/issues/601)
- Suppression des liens vers l'API Démarche Numérique pour les avis d'expert. [#5554cde](https://github.com/betagouv/pitchou/commit/5554cde)

### Évolutions techniques
- Refactorisation du dépôt en monorepo. [#593](https://github.com/betagouv/pitchou/issues/593), [#595](https://github.com/betagouv/pitchou/issues/595)
- Mise en place de Sentry pour la surveillance des applications instructeur et administrateur.
- Remplacement de l'identifiant Pitchou par le numéro de démarche numérique. [#639](https://github.com/betagouv/pitchou/issues/639)
- Correction du chemin du schéma Démarche Numérique pour le worker. [#603](https://github.com/betagouv/pitchou/issues/603)
- Correction de la synchronisation avec l'API Démarche Numérique en local.
- Nettoyage du code après la migration vers S3. [#598](https://github.com/betagouv/pitchou/issues/598)
- Suppression de la personne suivant le dossier si elle n'a pas accès au dossier. [#625](https://github.com/betagouv/pitchou/issues/625)
- Mise à jour du DPO dans la documentation sur les données personnelles. [#624](https://github.com/betagouv/pitchou/issues/624)

### Autres changements
- Mise à jour des modèles de documents pour la génération.
- Ajout de nouveaux fichiers de saisine CSRPN et de mail de saisine au CNPN.
- Documentation mise à jour par Audrey Bramy.
- Ajout de seeds plus réalistes pour les tests. [#608](https://github.com/betagouv/pitchou/issues/608)
- Ajout de seeds D10 et D11. [#623](https://github.com/betagouv/pitchou/issues/623)
- Ajout d'un bouton pour télécharger les événements métriques pour les statistiques AARRI. [#615](https://github.com/betagouv/pitchou/issues/615)
- Suppression de la date de dernière contribution dans les statistiques AARRI. [#615](https://github.com/betagouv/pitchou/issues/615)
- Ajout de pièces jointes dans les seeds. [#614](https://github.com/betagouv/pitchou/issues/614)
- Correction d'un typo dans la modale de saisie des espèces. [#614](https://github.com/betagouv/pitchou/issues/614)
- Correction du fuseau horaire des dates. [#612](https://github.com/betagouv/pitchou/issues/612)
- Ajout de la matrice d'impact à la page des statistiques. [#599](https://github.com/betagouv/pitchou/issues/599)
- Ajout du groupe instructeur dans le fichier CSV des événements métriques. [#633](https://github.com/betagouv/pitchou/issues/633)
- Ajout de l'accès au groupe instructeur pour chaque utilisateur. [#633](https://github.com/betagouv/pitchou/issues/633)
- Suppression des enjeux politiques et écologiques de la synchronisation avec l'API Démarche Numérique. [#605](https://github.com/betagouv/pitchou/issues/605)
- Suppression de l'historique des dates d'envoi de la dernière contribution. [#615](https://github.com/betagouv/pitchou/issues/615)
- Reset de la base de données et du S3 sur chaque déploiement en staging. [#621](https://github.com/betagouv/pitchou/issues/621)
