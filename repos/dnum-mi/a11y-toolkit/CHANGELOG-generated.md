## Changelog : a11y-toolkit (30 derniers jours, au 10 septembre 2026)

### Résumé
Le projet est passé de sa phase de création initiale à une version fonctionnelle et structurée. De nouveaux outils de vérification d'accessibilité (basés sur le DSFR) et un mode sombre ont été intégrés, tandis qu'un système de tests automatisés a été mis en place pour garantir la fiabilité des futures évolutions.

### Évolutions fonctionnelles
- Ajout de nouvelles pages de ressources : contrôles simplifiés (DSFR) et consultation des résultats [#1](https://github.com/dnum-mi/a11y-toolkit/pull/1).
- Intégration d'un sélecteur de thème (mode clair/sombre) [#1](https://github.com/dnum-mi/a11y-toolkit/pull/1).

### Évolutions techniques
- Mise en place de la chaîne CI/CD via GitHub Actions [#1](https://github.com/dnum-mi/a11y-toolkit/pull/1).
- Optimisation et correction des tests d'accessibilité `pa11y` en environnement de CI (gestion du sandbox et exclusion de liens bloquants) [#1](https://github.com/dnum-mi/a11y-toolkit/pull/1).
- Mise à jour de la version de Node.js et des actions pour prévenir les avertissements de dépréciation [#2](https://github.com/dnum-mi/a11y-toolkit/pull/2).
- Suppression du workflow de déploiement GitHub Pages.

### Autres changements
- Initialisation et enrichissement de la documentation (README) incluant des informations sur l'accessibilité.
- Ajout d'un lien vers la licence dans le pied de page.
