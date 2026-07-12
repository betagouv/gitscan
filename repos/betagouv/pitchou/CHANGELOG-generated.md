## Changelog : pitchou (30 derniers jours, au 10 juillet 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'expérience utilisateur, notamment pour les instructeurs et les administrateurs. Des fonctionnalités ont été ajoutées pour faciliter la gestion des dossiers, l'accès aux informations et le suivi des indicateurs clés. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- **Instructeur :**
    - Ajout d'une modale pour les pièces jointes aux dossiers [#634](https://github.com/betagouv/pitchou/issues/634).
    - Possibilité de contacter le dépositaire du dossier directement depuis l'interface [#630](https://github.com/betagouv/pitchou/issues/630).
    - Ajout d'un onglet "Porteur de projet" pour faciliter l'accès aux informations pertinentes [#627](https://github.com/betagouv/pitchou/issues/627).
    - Affichage des liens vers les documents associés aux espèces protégées [#635](https://github.com/betagouv/pitchou/issues/635).
    - Affichage et téléchargement de la cartographie associée aux dossiers [#629](https://github.com/betagouv/pitchou/issues/629).
- **Administration :**
    - Ajout de la possibilité d'assigner un groupe "instructeur" à chaque utilisateur [#633](https://github.com/betagouv/pitchou/issues/633).
    - Ajout d'un bouton pour télécharger les événements métriques des utilisateurs à des fins statistiques AARRI [#600](https://github.com/betagouv/pitchou/issues/600).
    - Page d'administration des utilisateurs avec indication du niveau AARRI [#591](https://github.com/betagouv/pitchou/issues/591).
    - Amélioration de la section évolution des indicateurs AARRI dans les statistiques [#597](https://github.com/betagouv/pitchou/issues/597).
- **Général :**
    - Remplacement de l'identifiant Pitchou par le numéro de démarche numérique [#639](https://github.com/betagouv/pitchou/issues/639).
    - Ajout de la prise en charge des fichiers .xlsx [#628](https://github.com/betagouv/pitchou/issues/628).
    - Ajout d'un bouton "retour" dans l'interface dossier [#609](https://github.com/betagouv/pitchou/issues/609).
    - Ajout d'un fil d'Ariane pour faciliter la navigation [#610](https://github.com/betagouv/pitchou/issues/610).
    - Possibilité d'éditer les dates de consultation du public dans l'onglet instruction [#600](https://github.com/betagouv/pitchou/issues/600).
    - Possibilité d'éditer le champ "enjeux" dans l'instruction [#604](https://github.com/betagouv/pitchou/issues/604).
    - Ajout d'une date de mise en service dans les dossiers (en préparation de la prochaine MEP) [#616](https://github.com/betagouv/pitchou/issues/616).

### Évolutions techniques
- Refactorisation du dépôt en monorepo [#593](https://github.com/betagouv/pitchou/issues/593) et [#595](https://github.com/betagouv/pitchou/issues/595).
- Migration de la liste des espèces protégées du CSV vers une table en base de données [#589](https://github.com/betagouv/pitchou/issues/589).
- Correction du chemin du schéma DS pour le worker [#603](https://github.com/betagouv/pitchou/issues/603).
- Suppression de la synchronisation des "enjeux politique et écologique" (annotation privée) depuis Démarches Numériques [#605](https://github.com/betagouv/pitchou/issues/605).
- Suppression des liens vers Démarches Numériques dans les avis d'expert [#596](https://github.com/betagouv/pitchou/issues/596).
- Amélioration de la gestion des fuseaux horaires des dates [#612](https://github.com/betagouv/pitchou/issues/612).
- Reset de la base de données et du S3 sur chaque déploiement en staging [#621](https://github.com/betagouv/pitchou/issues/621).
- Correction de la synchronisation avec Démarches Numériques en local [#625](https://github.com/betagouv/pitchou/issues/625).

### Autres changements
- Mise à jour de la documentation concernant le Délégué à la Protection des Données [#642](https://github.com/betagouv/pitchou/issues/642).
- Ajout de domaines PACA autorisés pour l'authentification [#641](https://github.com/betagouv/pitchou/issues/641).
- Ajout de domaines autorisés pour l'authentification [#637](https://github.com/betagouv/pitchou/issues/637).
- Ajout d'une erreur lors de la tentative de connexion avec un domaine non autorisé [#602](https://github.com/betagouv/pitchou/issues/602).
- Ajout de seeds (données de test) pour les dossiers D10 et D11 [#623](https://github.com/betagouv/pitchou/issues/623).
- Enrichissement des seeds avec des dossiers plus réalistes [#608](https://github.com/betagouv/pitchou/issues/608).
- Ajout de pièces jointes dans les seeds [#614](https://github.com/betagouv/pitchou/issues/614).
- Correction de typos dans la modal de saisie des espèces [#615](https://github.com/betagouv/pitchou/issues/615).
- Mise à jour des modèles pour la génération de documents et ajout de nouveaux fichiers de saisine [#640](https://github.com/betagouv/pitchou/issues/640).
- Mise à jour du DPO dans la documentation [#624](https://github.com/betagouv/pitchou/issues/624).
