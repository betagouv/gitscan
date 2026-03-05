## Changelog : mon-entreprise (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées au site mon-entreprise au cours des 30 derniers jours. Les principales évolutions concernent le comparateur de statuts, avec l'ajout de nouvelles informations sur les droits à la retraite, ainsi que des corrections et améliorations techniques, notamment en matière d'accessibilité et de conformité aux normes. Une implémentation de la réforme RGDU pour les salariés a également été réalisée.

### Évolutions fonctionnelles
- Ajout du lien vers le simulateur de l'Assurance retraite dans le comparateur de statuts. [#4323](https://github.com/betagouv/mon-entreprise/issues/4323)
- Ajout de la comparaison du revenu cotisé dans le comparateur de statuts.
- Remplacement des montants retraite par des trimestres et des points dans le comparateur.
- Harmonisation des unités pour les trimestres et points acquis annuellement dans le comparateur.
- Correction de l'affichage mobile du montant des cotisations. [#4290](https://github.com/betagouv/mon-entreprise/issues/4290)
- Implémentation de la réforme RGDU pour les salariés.
- Mise à jour de la déduction forfaitaire sur les heures supplémentaires pour les salariés.
- Ajout de la CET dans la base de l'exonération des heures supplémentaires.
- Suppression du lien vers le simulateur Cnav du comparateur.
- Suppression de l'objectif retraite de base de la config comparateur.
- Suppression de l'ACRE de la condition bloquant l'affichage des droits retraite.
- Suppression des objectifs de projection retraite base et complémentaire de la config PL.

### Évolutions techniques
- Refactorisation de l'accès à `document.location` dans un `useEffect`.
- Amélioration du typage de nouveaux champs.
- Suppression de props inutilisés dans les composants `Questions` et `RadioGroup`.
- Correction de typos et d'imports implicites dans `AnswersList`.
- Remplacement de `inIframe()` par `theme.isInIframe` au niveau module.
- Remplacement de `console.error` par `Sentry.captureException` dans `colors.tsx`.
- Ajout de guards `typeof window` dans `useIsEmbedded`.
- Mise à jour des tests unitaires de l'API.
- Suppression de l'avertissement lié à la réforme RGDU non implémentée.
- Mise à jour des références pour l'exonération salariale sur les heures supplémentaires.

### Autres changements
- Mise à jour du changelog pour le modèle social.
- Amélioration significative de la documentation sur l'accessibilité, incluant des règles, des exemples et des liens vers des ressources utiles.
- Mise à jour des traductions (i18n).
- Correction de problèmes de linting.
- Mise à jour de la déclaration d'accessibilité suite aux audits.
- Remplacement d'un tableau par une liste pour améliorer l'accessibilité.
- Précision de la documentation concernant les droits à la retraite (dépendance du montant cotisé).
- Ajout de la date aux questions de la liste noire.
