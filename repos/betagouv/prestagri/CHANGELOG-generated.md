## Changelog : prestagri (30 derniers jours, au 2026-06-19)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'implémentation et le déploiement de nouvelles fonctionnalités liées au calcul de l'aide scolaire, notamment le calcul du quotient familial et l'intégration de données provenant de la DN (Direction Nationale). Plusieurs déploiements ont été effectués pour rendre ces fonctionnalités disponibles.

### Évolutions fonctionnelles
- Implémentation du calcul du quotient familial pour l'aide scolaire.
- Intégration de données d'adresse provenant de la DN [#1234](https://github.com/betagouv/prestagri/issues/1234).
- Déploiement de la calculatrice d'aide scolaire sur GitHub.
- Déploiement de l'aide scolaire sans prise en compte du trajet.
- Retour de données au format JSON pour la DN.
- Ajout d'un quotient familial spécial pour l'aide scolaire.

### Évolutions techniques
- Remplacement du package Catala par un module généré.
- Utilisation de Python généré dans l'application web.
- Nettoyage du code lié au calcul du quotient familial.

### Autres changements
- Correction d'une erreur d'import.
- Amélioration de la documentation de la page Catala.
