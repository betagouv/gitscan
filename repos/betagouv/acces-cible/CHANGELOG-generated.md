## Changelog : acces-cible (30 derniers jours, au 15 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilisation des imports CSV, l'ajout d'un nouveau widget JDMA, et des optimisations techniques pour améliorer la performance et la maintenance de l'application. Des corrections ont également été apportées pour éviter les doublons de tags et normaliser les URLs des sites.

### Évolutions fonctionnelles
- Ajout d'un widget JDMA pour faciliter l'utilisation de l'application. [#569](https://github.com/betagouv/acces-cible/issues/569)
- Correction d'un bug qui provoquait des doublons de tags lors de l'import de fichiers CSV. [#577](https://github.com/betagouv/acces-cible/issues/577)
- Normalisation de l'URL des sites pour garantir une cohérence des données. [#576](https://github.com/betagouv/acces-cible/issues/576)
- Stabilisation des imports CSV en les traitant en arrière-plan pour une meilleure expérience utilisateur. [#541](https://github.com/betagouv/acces-cible/issues/541)
- Configuration du bouton JDMA via des variables d'environnement pour une plus grande flexibilité. [#578](https://github.com/betagouv/acces-cible/issues/578)

### Évolutions techniques
- Refactor du navigateur utilisé par l'application. [#545](https://github.com/betagouv/acces-cible/issues/545)
- Correction de requêtes SQL N+1 pour améliorer la performance. [#538](https://github.com/betagouv/acces-cible/issues/538)
- Utilisation du composant DSFR Side Menu pour améliorer l'interface utilisateur. [#571](https://github.com/betagouv/acces-cible/issues/571)
- Mise à jour de la configuration de la file d'attente (queue.yml) pour corriger une faute de frappe. [#567](https://github.com/betagouv/acces-cible/issues/567)
- Suppression de code lié à l'historisation (`audits`) pour simplifier la base de données. [#580](https://github.com/betagouv/acces-cible/issues/580), [#582](https://github.com/betagouv/acces-cible/issues/582), [#573](https://github.com/betagouv/acces-cible/issues/573)
- Mise à jour du Dockerfile pour utiliser la configuration correcte. [#547](https://github.com/betagouv/acces-cible/issues/547)
- Suppression d'une version personnalisée d'Omniauth. [#587](https://github.com/betagouv/acces-cible/issues/587)
- Amélioration du mocking des tests Axe pour une meilleure fiabilité. [#586](https://github.com/betagouv/acces-cible/issues/586)

### Autres changements
- Aucune information supplémentaire à signaler.
