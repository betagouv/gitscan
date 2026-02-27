## Changelog : mon-entreprise (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées au site mon-entreprise au cours des 30 derniers jours. Les principales évolutions concernent le comparateur de statuts, avec l'ajout d'informations sur la retraite et la simplification de l'affichage. Des corrections et des améliorations ont également été apportées concernant le calcul des cotisations sociales, notamment pour les salariés et les heures supplémentaires. Enfin, la documentation sur l'accessibilité a été considérablement enrichie.

### Évolutions fonctionnelles

- **Comparateur de statuts :**
    - Ajout du lien vers le simulateur de l'Assurance retraite (#4323).
    - Ajout de la comparaison du revenu cotisé.
    - Remplacement des montants retraite par des informations sur les trimestres et points acquis.
    - Harmonisation des unités pour les trimestres et points acquis.
- **Droits retraite :**
    - Ajout d'un lien vers le simulateur de retraite de la Cnav.
    - Simplification de l'affichage des droits retraite.
- **Calcul des cotisations sociales (salarié) :**
    - Implémentation de la réforme RGDU.
    - Mise à jour de la déduction forfaitaire sur les heures supplémentaires.
    - Ajout de la CET dans la base de l'exonération des heures supplémentaires.
    - Correction de l'affichage mobile du montant des cotisations (#4290).
- **Cessation d'activité :**
    - Remplacement du switch IR/IS par une question explicite.
    - Utilisation de composants d'interface plus récents (SimpleField et SwitchContainer).
    - Précision que la rémunération inclut les cotisations et contributions.

### Évolutions techniques

- **Refactor :**
    - Évaluation directe des conditions dans `DetailsRowCards`.
    - Remplacement de `inIframe()` par `theme.isInIframe`.
    - Suppression de la fonction `inIframe` obsolète.
    - Ajout d'un guard `typeof window` dans `useIsEmbedded`.
    - Déplacement de l'accès à `document.location` dans un `useEffect`.
- **Documentation :**
    - Amélioration de la documentation sur l'accessibilité avec des règles issues des audits et des outils de vérification.
- **Divers :**
    - Remplacement de `console.error` par `Sentry.captureException` dans `colors.tsx`.

### Autres changements

- **Documentation :** Précision que les droits à la retraite dépendent du montant cotisé.
- **Tests :** Mise à jour des tests unitaires de l'API.
- **Chore :** Suppression des taux réduits AF et AM hors Lodeom.
- **Chore :** Suppression de l'avertissement concernant la réforme RGDU non implémentée.
- **Fix :** Ajout de la date aux questions de la liste noire.
- **Fix :** Suppression de la projection de montant de retraite des simulateurs indépendants.
- **Fix :** Retrait de l'ACRE de la condition bloquant l'affichage des droits retraite.
- **Fix :** Suppression des objectifs de projection retraite base et complémentaire de la config PL.
- **Linting :** Exécution de `lint:fix`.
- **i18n :** Mise à jour des traductions.
- **Accessibilité :**
    - Mise à jour de la déclaration d'accessibilité suite aux audits.
    - Remplacement d'un tableau par une liste pour améliorer l'accessibilité.
