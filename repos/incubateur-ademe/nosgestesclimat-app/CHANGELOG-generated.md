## Changelog : nosgestesclimat-app (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur une refonte architecturale majeure vers une structure monorepo, améliorant la maintenabilité et la scalabilité du projet. Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées, notamment au niveau du suivi des données, de l'affichage des simulations et de la gestion des bannières. Enfin, des améliorations ont été faites pour faciliter le développement local avec l'introduction de devcontainers.

### Évolutions fonctionnelles
- Ajout d'un bouton "Je ne sais pas" en test A/B dans le questionnaire, pour améliorer l'expérience utilisateur. [#1737](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1737)
- Suppression de la simulation depuis l'espace personnel. [#1747](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1747)
- Ajout d'une bannière JVA (Justice Verte et Agriculture) avec une logique d'affichage corrigée. [#1748](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1748) et [#1749](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1749)
- Correction de l'affichage de l'ordre des points sur les graphiques. [#1780](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1780)
- Correction de l'affichage des noms des participants et administrateurs. [#1773](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1773)
- Correction du blocage du bouton "Terminer" après avoir répondu à toutes les questions. [#1776](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1776)
- Ajout d'un feature flag pour les actions. [#1775](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1775)

### Évolutions techniques
- Refonte de l'architecture vers un monorepo pour une meilleure organisation et maintenabilité. [#1745](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1745)
- Migration de l'ORM vers le core NGC. [#1771](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1771)
- Mise en place de devcontainers pour faciliter le développement local. [#1751](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1751)
- Amélioration du script de déploiement et correction des tests associés.
- Correction de problèmes de build et de déploiement sur l'environnement de pré-production (suppression temporaire du déploiement en pré-production). [#1787](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1787)
- Amélioration du suivi des données (correction du tracking de Matomo et de l'iframe). [#1782](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1782) et [#1783](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1783)
- Correction d'une erreur dans la configuration de `tsconfigRootDir`. [#1757](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1757)
- Mise à jour des workflows CI/CD et des configurations ESLint. [#1765](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1765)

### Autres changements
- Ajout de traductions. [#1769](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1769)
- Correction d'un bug permettant l'utilisation de l'opérateur `!=` dans les conditions des funfacts. [#1755](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1755)
- Amélioration du contraste de l'interface utilisateur dans l'IDE.
- Suppression de fichiers inutiles (yarnrc, pnpm-store).
- Correction de logs et gestion des erreurs de session.
- Mise à jour de la documentation et des configurations.
