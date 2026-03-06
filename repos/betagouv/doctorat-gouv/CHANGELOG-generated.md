## Changelog : doctorat-gouv (30 derniers jours)

### Résumé
Cette version apporte des améliorations significatives à l'interface utilisateur, notamment au niveau de la navigation mobile, du footer et de la page de contact. Des corrections de bugs ont été apportées pour améliorer l'affichage et la réactivité de certains éléments. Des fonctionnalités importantes ont été ajoutées, comme l'affichage des pièces jointes des sujets de thèse, l'activation/désactivation des sujets en fonction d'ADUM, et l'ajout d'un filtre de recherche par numéro d'école doctorale. La conformité RGPD a également été renforcée avec l'anonymisation des logs.

### Évolutions fonctionnelles
- Ajout de l'affichage des pièces jointes des sujets de thèse. [#8](https://github.com/betagouv/doctorat-gouv/pull/8)
- Ajout d'un filtre de recherche par numéro d'école doctorale. [#7](https://github.com/betagouv/doctorat-gouv/pull/7)
- Permettre l'activation et la désactivation des sujets de thèse en fonction de la réponse d'ADUM. [#6](https://github.com/betagouv/doctorat-gouv/pull/6)
- Amélioration de la page de contact pour une meilleure réactivité.
- Affichage du nombre de résultats de recherche, même en cas d'absence de résultats.
- Ajout d'une info-bulle informant sur le canal de contact privilégié.
- Ajout du numéro de version dans le footer.
- Ajout d'une nouvelle URL de recherche sur le code ROR de l'établissement.
- Modification du menu header.
- Ajout d'un message concernant le canal le plus optimisé pour une bonne expérience utilisateur.
- Modification du bouton "Envoyer" pour l'aligner à droite.
- Modification du menu "Retour à l'accueil".
- Ajout d'icônes DSF dans le menu mobile.

### Évolutions techniques
- Anonymisation des logs pour garantir la conformité RGPD.
- Modification de la planification du scheduler ADUM pour les environnements de développement et de recette.
- Amélioration de la résolution du logo de la plateforme.
- Correction du problème d'arrière-plan du logo Marianne.
- Modification du filtre de localisation pour afficher toutes les régions.

### Autres changements
- Améliorations de l'affichage du menu mobile.
- Améliorations responsives du footer.
- Réduction de la taille de l'info-bulle sur la page de recherche.
- Modification du surlignage de l'info-bulle.
- Ajout d'un fichier `burger.svg` pour le menu mobile.
- Amélioration de la réactivité du header.
- Ajout d'une info-banner.
- Préparation des versions 0.2.1 et 0.2.2.
- Finalisation des versions 0.2.0, 0.2.1 et 0.2.2.
