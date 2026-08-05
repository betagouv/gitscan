## Changelog : acceslibre (30 derniers jours, au 03/08/2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment via l'optimisation du parcours de signalement et la clarté des informations liées au régime de protection de l'autonomie (RPA). La plateforme bénéficie également de renforcements techniques pour améliorer la surveillance du système et la sécurité du traitement des données.

### Évolutions fonctionnelles
- **Parcours de signalement** : Amélioration de l'interface utilisateur incluant la mise à jour de la fenêtre modale, des messages de succès et de la logique de la page de confirmation [#2713](https://github.com/MTES-MCT/acceslibre/pull/2713), [#2714](https://github.com/MTES-MCT/acceslibre/pull/2714).
- **Affichage et terminologie** : Optimisation de l'affichage du badge et des libellés concernant le RPA (Régime de Protection de l'Autonomie) [#2711](https://github.com/MTES-MCT/acceslibre/pull/2711), [#2715](https://github.com/MTES-MCT/acceslibre/pull/2715).
- **Internationalisation** : Correction de l'affichage du bouton de traduction [#2726](https://github.com/MTES-MCT/acceslibre/pull/2726) et ajout de la possibilité de traduire le champ d'accessibilité à la demande [#2692](https://github.com/MTES-MCT/acceslibre/pull/2692).
- **Gestion des données établissements** : Possibilité de modifier la date de dernière vérification lors de la création, de l'édition ou de l'import d'un établissement (ERP) [#2712](https://github.com/MTES-MCT/acceslibre/pull/2712).

### Évolutions techniques
- **Maintenance et sécurité** : Mise à jour mineure du framework Django [#2716](https://github.com/MTES-MCT/acceslibre/pull/2716) et remplacement de la bibliothèque de nettoyage `bleach` par `nh3` pour une meilleure gestion des contenus [#2744](https://github.com/MTES-MCT/acceslibre/pull/2744).
- **Observabilité et infrastructure** : Intégration du suivi de l'état du cache dans Sentry pour un meilleur monitoring [#2727](https://github.com/MTES-MCT/acceslibre/pull/2727) et ajustement du mappage des ports pour l'utilisation de Docker [#2728](https://github.com/MTES-MCT/acceslibre/pull/2728).
