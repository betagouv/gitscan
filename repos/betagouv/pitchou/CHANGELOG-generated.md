## Changelog : pitchou (30 derniers jours, au 15 juillet 2026)

### Résumé
Ce mois-ci, l'équipe a continué d'améliorer l'expérience utilisateur et la robustesse de Pitchou. Les principales évolutions concernent l'interface instructeur, avec l'ajout de fonctionnalités pour consulter les pièces jointes, la cartographie et contacter le porteur de projet. Des améliorations ont également été apportées à la synchronisation avec Démarche Numérique, à la gestion des utilisateurs et aux statistiques AARRI. Une refonte de l'architecture du dépôt en monorepo a été initiée.

### Évolutions fonctionnelles
- **Instructeur :**
    - Ajout de la possibilité de télécharger la cartographie associée au dossier [#629](https://github.com/betagouv/pitchou/issues/629).
    - Possibilité de contacter le déposant du dossier directement depuis l'interface [#630](https://github.com/betagouv/pitchou/issues/630).
    - Ajout d'un onglet "Porteur de projet" [#627](https://github.com/betagouv/pitchou/issues/627).
    - Correction de la réactivité de la date des prescriptions et rafraîchissement du dossier en cache [#648](https://github.com/betagouv/pitchou/issues/648), [#649](https://github.com/betagouv/pitchou/issues/649).
    - Suppression du lien vers les annotations privées [#636](https://github.com/betagouv/pitchou/issues/636).
    - Ajout d'une modale pour les pièces jointes [#634](https://github.com/betagouv/pitchou/issues/634).
- **Synchronisation Démarche Numérique :**
    - Correction de la sélection GraphQL pour la géométrie [#632](https://github.com/betagouv/pitchou/issues/632).
    - Correction pour assurer le bon fonctionnement de la synchronisation en local [#620](https://github.com/betagouv/pitchou/issues/620).
    - Le numéro de dossier Démarche Numérique remplace l'identifiant Pitchou dans les modèles de documents [#639](https://github.com/betagouv/pitchou/issues/639) et [#7303f59](https://github.com/betagouv/pitchou/commit/7303f59).
- **Authentification :**
    - Ajout de domaines PACA autorisés pour l'authentification [#641](https://github.com/betagouv/pitchou/issues/641) et [#637](https://github.com/betagouv/pitchou/issues/637).
    - Autorisation du domaine ext.beta.gouv.fr [#601](https://github.com/betagouv/pitchou/issues/601).
    - Affichage d'une erreur si le domaine utilisé pour la connexion n'est pas autorisé [#602](https://github.com/betagouv/pitchou/issues/602).
- **Administration :**
    - Ajout d'un groupe "instructeur" pour la gestion des accès utilisateurs [#633](https://github.com/betagouv/pitchou/issues/633).
    - Possibilité de télécharger les événements métriques pour les statistiques AARRI [#620](https://github.com/betagouv/pitchou/issues/620).
    - Page utilisateurs avec le niveau AARRI [#591](https://github.com/betagouv/pitchou/issues/591).
- **Espèces protégées :**
    - Affichage des liens vers les documents associés aux espèces protégées [#635](https://github.com/betagouv/pitchou/issues/635).
    - Acceptation des fichiers .xlsx pour la liste des espèces protégées [#628](https://github.com/betagouv/pitchou/issues/628).
    - Migration de la liste des espèces protégées du CSV vers une table en base de données [#589](https://github.com/betagouv/pitchou/issues/589).

### Évolutions techniques
- **Architecture :**
    - Refonte du dépôt en monorepo (premières étapes) [#593](https://github.com/betagouv/pitchou/issues/593) et [#595](https://github.com/betagouv/pitchou/issues/595).
- **Infrastructure :**
    - Reset de la base de données et du S3 sur chaque déploiement en staging [#621](https://github.com/betagouv/pitchou/issues/621).
    - Nettoyage du code après la migration vers S3 [#598](https://github.com/betagouv/pitchou/issues/598).
- **Divers :**
    - Correction du fuseau horaire des dates [#612](https://github.com/betagouv/pitchou/issues/612).
    - Correction du chemin du schéma Démarche Numérique [#603](https://github.com/betagouv/pitchou/issues/603).

### Autres changements
- Mise à jour de la documentation concernant le délégué à la protection des données [#642](https://github.com/betagouv/pitchou/issues/642).
- Mise à jour des modèles de documents pour la génération [#5f8e0f5](https://github.com/betagouv/pitchou/commit/5f8e0f5).
- Ajout de nouveaux fichiers de saisine CSRPN et de mail au CNPN [#cceb51d](https://github.com/betagouv/pitchou/commit/cceb51d) et [#0ea9e0d](https://github.com/betagouv/pitchou/commit/0ea9e0d).
- Suppression de la synchronisation des "enjeux politique et écologique" depuis Démarche Numérique [#605](https://github.com/betagouv/pitchou/issues/605).
- Suppression de l'historique de la date d'envoi de la dernière contribution [#615](https://github.com/betagouv/pitchou/issues/615).
- Ajout de pièces jointes aux seeds [#614](https://github.com/betagouv/pitchou/issues/614).
- Enrichissement des seeds avec des dossiers plus réalistes [#608](https://github.com/betagouv/pitchou/issues/608).
- Typo corrigée dans la modale de saisie des espèces [#c8d4c6a](https://github.com/betagouv/pitchou/commit/c8d4c6a).
- Ajout d'une page d'erreur 404 personnalisée [#596](https://github.com/betagouv/pitchou/issues/596).
- Amélioration de la section évolution des indicateurs AARRI [#597](https://github.com/betagouv/pitchou/issues/597).
- Correction de la suppression de décision [#588](https://github.com/betagouv/pitchou/issues/588).
- Ajout d'un bouton "retour" dans l'interface dossier [#609](https://github.com/betagouv/pitchou/issues/609).
- Ajout d'un fil d'Ariane [#610](https://github.com/betagouv/pitchou/issues/610).
- Suppression de liens vers Démarche Numérique dans les avis d'expert [#5554cde](https://github.com/betagouv/pitchou/commit/5554cde).
- Possibilité d'éditer le champ "enjeux" [#604](https://github.com/betagouv/pitchou/issues/604).
- Les dates de consultation du public sont maintenant éditables [#600](https://github.com/betagouv/pitchou/issues/600).
- Correction de la suppression de personne suite à un dossier [#625](https://github.com/betagouv/pitchou/issues/625).
- Mise à jour du DPO dans la documentation [#624](https://github.com/betagouv/pitchou/issues/624).
- Ajout de dossiers D10 et D11 aux seeds [#623](https://github.com/betagouv/pitchou/issues/623).
- Ajout de seeds en staging [#620](https://github.com/betagouv/pitchou/issues/620).
