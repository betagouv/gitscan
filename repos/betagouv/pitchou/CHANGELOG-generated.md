## Changelog : pitchou (30 derniers jours, au 09 juillet 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur, notamment en facilitant l'accès aux informations des dossiers, en améliorant la gestion des pièces jointes et en ajoutant des fonctionnalités pour les instructeurs. Des efforts importants ont également été consacrés à l'infrastructure et à la synchronisation des données, ainsi qu'à l'amélioration des statistiques et du suivi des utilisateurs.

### Évolutions fonctionnelles
- Ajout d'une modale pour les pièces jointes dans les dossiers [#634](https://github.com/betagouv/pitchou/issues/634).
- Affichage des liens des documents associés aux espèces protégées [#635](https://github.com/betagouv/pitchou/issues/635).
- Possibilité de contacter le porteur de projet directement depuis l'entête du dossier [#630](https://github.com/betagouv/pitchou/issues/630).
- Ajout d'un onglet "Porteur de projet" dans les dossiers [#627](https://github.com/betagouv/pitchou/issues/627).
- Ajout d'un bouton "Retour" dans les dossiers [#609](https://github.com/betagouv/pitchou/issues/609).
- Ajout d'un fil d'Ariane pour faciliter la navigation [#610](https://github.com/betagouv/pitchou/issues/610).
- Possibilité d'éditer les dates de consultation du public dans l'onglet instruction [#600](https://github.com/betagouv/pitchou/issues/600).
- Possibilité d'éditer le champ "enjeux" dans l'instruction [#604](https://github.com/betagouv/pitchou/issues/604).
- Ajout de la prise en charge des fichiers .xlsx pour les espèces protégées [#628](https://github.com/betagouv/pitchou/issues/628).
- Ajout de domaines PACA autorisés pour l'authentification [#641](https://github.com/betagouv/pitchou/issues/641) et [#637](https://github.com/betagouv/pitchou/issues/637).
- Affichage d'une erreur si le domaine de connexion n'est pas autorisé [#602](https://github.com/betagouv/pitchou/issues/602).
- Suppression des liens vers les démarches numériques dans les avis d'expert [#595](https://github.com/betagouv/pitchou/issues/595).

### Évolutions techniques
- Refactorisation du dépôt en monorepo [#593](https://github.com/betagouv/pitchou/issues/593) et [#595](https://github.com/betagouv/pitchou/issues/595).
- Migration de la liste des espèces protégées du CSV vers une table en base de données [#589](https://github.com/betagouv/pitchou/issues/589).
- Correction du chemin du schéma DS pour le worker [#603](https://github.com/betagouv/pitchou/issues/603).
- Correction du fuseau horaire des dates [#612](https://github.com/betagouv/pitchou/issues/612).
- Amélioration de la synchronisation avec la démarche numérique (DN) [#620](https://github.com/betagouv/pitchou/issues/620), [#632](https://github.com/betagouv/pitchou/issues/632), et plusieurs réversions/corrections de la synchronisation.
- Reset de la base de données et du S3 à chaque déploiement en staging [#621](https://github.com/betagouv/pitchou/issues/621).
- Ajout de seeds plus réalistes pour les tests [#608](https://github.com/betagouv/pitchou/issues/608).
- Suppression de la personne qui suit un dossier si elle n'y a plus accès [#625](https://github.com/betagouv/pitchou/issues/625).

### Autres changements
- Mise à jour de la documentation concernant le délégué à la protection des données [#642](https://github.com/betagouv/pitchou/issues/642).
- Mise à jour du DPO dans la documentation [#624](https://github.com/betagouv/pitchou/issues/624).
- Ajout de nouveaux modèles pour la génération de documents et de nouveaux fichiers de saisine [#616](https://github.com/betagouv/pitchou/issues/616), [#5f8e0f5](https://github.com/betagouv/pitchou/commit/5f8e0f5), [#cceb51d](https://github.com/betagouv/pitchou/commit/cceb51d), [#0ea9e0d](https://github.com/betagouv/pitchou/commit/0ea9e0d), [#0c466ff](https://github.com/betagouv/pitchou/commit/0c466ff).
- Ajout de la possibilité de télécharger les événements métriques pour les statistiques AARRI [#607](https://github.com/betagouv/pitchou/issues/607).
- Amélioration de la section évolution des indicateurs AARRI dans les statistiques [#597](https://github.com/betagouv/pitchou/issues/597).
- Ajout d'une page d'erreur 404 personnalisée [#596](https://github.com/betagouv/pitchou/issues/596).
- Ajout d'une page utilisateurs avec le niveau AARRI [#591](https://github.com/betagouv/pitchou/issues/591).
- Ajout de la matrice d'impact à la page des statistiques [#599](https://github.com/betagouv/pitchou/issues/599).
- Suppression de l'historique de la date d'envoi de la dernière contribution [#615](https://github.com/betagouv/pitchou/issues/615).
- Ajout de pièces jointes aux seeds [#614](https://github.com/betagouv/pitchou/issues/614).
- Ajout de dossiers D10 et D11 aux seeds [#623](https://github.com/betagouv/pitchou/issues/623).
- Suppression de la synchronisation des annotations privées "enjeux politique et écologique" [#605](https://github.com/betagouv/pitchou/issues/605).
