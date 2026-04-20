## Changelog : sparte (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur une refonte majeure de la page d'accueil pour une meilleure expérience utilisateur, des corrections de bugs et des améliorations de la documentation. Des optimisations techniques ont également été apportées, notamment au niveau du déploiement et des tests.

### Évolutions fonctionnelles
- **Page d'accueil refondue** : Nouvelle conception de la page d'accueil avec une section "héros" repensée, des cartes produits améliorées, une barre de recherche "sticky" et des animations pour une expérience plus engageante [#1534](https://github.com/MTES-MCT/sparte/issues/1534).
- **Amélioration des libellés KPI** : Raccourcissement du libellé "Consommation d'espaces NAF cible" pour une meilleure lisibilité [#8d8716a3](https://github.com/MTES-MCT/sparte/commit/8d8716a3).
- **Nombre total de diagnostics** : Ajout du nombre total de diagnostics à la section "héros" de la page d'accueil.
- **Correction de l'affichage des étiquettes négatives** : Correction d'un problème d'affichage des étiquettes négatives dans le panneau latéral OcsgeDiffSidePanel [#1511](https://github.com/MTES-MCT/sparte/issues/1511).
- **Correction de la suppression des références secondaires** : Correction d'un bug empêchant la suppression correcte des références secondaires [#1542](https://github.com/MTES-MCT/sparte/issues/1542).

### Évolutions techniques
- **Amélioration de la santé des conteneurs Docker** : Ajout de vérifications de santé pour le service de base de données et modification des dépendances des services pour garantir un démarrage correct [#1523](https://github.com/MTES-MCT/sparte/issues/1523).
- **Refactoring des vues API** : Refactorisation de `UserLandPreferenceAPIView` pour utiliser `APIView` et mise à jour de la gestion des réponses [#1526](https://github.com/MTES-MCT/sparte/issues/1526).
- **Suppression de code obsolète DBT** : Suppression de fichiers SQL et YAML obsolètes pour les modèles d'artificialisation et d'imperméabilisation [#c0727db6](https://github.com/MTES-MCT/sparte/commit/c0727db6).
- **Correction du Makefile** : Suppression de la commande `docker compose down` du Makefile pour éviter une suppression accidentelle de la base de données en local [#1532](https://github.com/MTES-MCT/sparte/issues/1532).
- **Amélioration des tests** : Utilisation de `pytest.approx` pour les assertions de `target_2031` dans les tests et ajustement de la tolérance de différence absolue dans le test de flux d'artificialisation nette.
- **Suppression de la génération de documentation DBT** : Suppression de la génération de documents DBT du workflow de déploiement Airflow [#1524](https://github.com/MTES-MCT/sparte/issues/1524).

### Autres changements
- **Documentation mise à jour** : Mise à jour de la documentation avec des informations sur COG OCSGE et MAJIC [#1528](https://github.com/MTES-MCT/sparte/issues/1528).
- **Correction de la gestion du cache** : Correction d'un problème de cache busting [#1545](https://github.com/MTES-MCT/sparte/issues/1545).
- **Nettoyage de code** : Diverses opérations de nettoyage de code et suppression de fichiers inutilisés.
- **Correction CSRF** : Correction d'un problème lié à la protection CSRF [#1525](https://github.com/MTES-MCT/sparte/issues/1525).
- **Ajout de tests SQL** : Ajout de tests SQL pour vérifier la présence de tous les "lands" [#1517](https://github.com/MTES-MCT/sparte/issues/1517).
- **Correction d'un commentaire** : Correction d'un commentaire dans le code source concernant la différence de stock d'artificialisation [#1527](https://github.com/MTES-MCT/sparte/issues/1527).
