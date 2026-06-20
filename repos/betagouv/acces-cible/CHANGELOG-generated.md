## Changelog : acces-cible (30 derniers jours, au 26 juin 2024)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilisation des imports CSV, l'ajout d'un nouveau widget JDMA pour faciliter l'identification des problèmes d'accessibilité, et des optimisations techniques concernant la gestion des audits et l'environnement Docker. Des corrections ont également été apportées pour éviter les doublons de tags lors de l'import CSV et normaliser l'URL des sites.

### Évolutions fonctionnelles
- Ajout d'un widget JDMA pour afficher les résultats de tests d'accessibilité directement dans l'interface utilisateur. [#569](https://github.com/betagouv/acces-cible/issues/569)
- Possibilité de configurer le bouton JDMA via des variables d'environnement. [#578](https://github.com/betagouv/acces-cible/issues/578)
- Correction d'un bug qui provoquait des doublons de tags lors de l'import de fichiers CSV. [#577](https://github.com/betagouv/acces-cible/issues/577)
- L'URL des sites est maintenant normalisée pour assurer une meilleure cohérence des données. [#576](https://github.com/betagouv/acces-cible/issues/576)
- Stabilisation des imports CSV en les traitant en arrière-plan, améliorant ainsi la réactivité de l'application. [#541](https://github.com/betagouv/acces-cible/issues/541)

### Évolutions techniques
- Refactorisation du navigateur utilisé pour les tests. [#545](https://github.com/betagouv/acces-cible/issues/545)
- Suppression de la colonne `url` et `current` de la table `audits` et de la logique associée, simplifiant ainsi la structure de la base de données. [#582](https://github.com/betagouv/acces-cible/issues/582), [#580](https://github.com/betagouv/acces-cible/issues/580), [#573](https://github.com/betagouv/acces-cible/issues/573)
- Mise à jour de la configuration Docker pour utiliser le Dockerfile principal. [#547](https://github.com/betagouv/acces-cible/issues/547)
- Suppression d'une version personnalisée d'Omniauth, revenant à la version standard. [#587](https://github.com/betagouv/acces-cible/issues/587)
- Amélioration du mocking des tests Axe pour une meilleure fiabilité. [#586](https://github.com/betagouv/acces-cible/issues/586)
