## Changelog : seves (30 derniers jours, au 9 juillet 2026)

### Résumé
Ce changelog présente les améliorations apportées à Sèves au cours des 30 derniers jours. Les principales évolutions concernent l'amélioration de l'interface utilisateur, notamment avec l'introduction d'un nouveau composant de sélection arborescente (treeselect) pour filtrer les événements, ainsi que des corrections de bugs et des optimisations pour une meilleure expérience utilisateur, en particulier dans les modules d'investigation TIAC et SSA.

### Évolutions fonctionnelles
- Implémentation d'un nouveau composant de sélection arborescente (treeselect) pour filtrer les événements dans les modules SSA et produits, disponible pour tous les utilisateurs. [#ad56c3b](https://github.com/betagouv/seves/pull/ad56c3b)
- Ajout d'un bouton pour désélectionner tous les éléments dans le composant treeselect. [#3b1a0c1](https://github.com/betagouv/seves/pull/3b1a0c1)
- Pré-remplissage automatique du formulaire de conclusion pour certains types d'événements (Repas, Aliment Suspect). [#20992f3](https://github.com/betagouv/seves/pull/20992f3), [#4bb0f38](https://github.com/betagouv/seves/pull/4bb0f38)
- Ajout de l'organisme nuisible dans le module SV. [#a3ed15e](https://github.com/betagouv/seves/pull/a3ed15e)
- Amélioration de l'affichage de la catégorie de danger pour les ICH (Intoxication Collective Alimentaire) dans la vue SSA. [#4c76f7e](https://github.com/betagouv/seves/pull/4c76f7e)
- Envoi de notifications DI (Déclaration d'Incident) aux agents concernés. [#ccb07a5](https://github.com/betagouv/seves/pull/ccb07a5)
- Harmonisation de la formulation de la navigation dans le module SV. [#14faf48](https://github.com/betagouv/seves/pull/14faf48)
- Ajout d'un champ "Date de réception" obligatoire pour les investigations TIAC. [#d0b54a9](https://github.com/betagouv/seves/pull/d0b54a9)
- Ajout d'un tooltip sur la description dans la vue liste SSA. [#0ee03fc](https://github.com/betagouv/seves/pull/0ee03fc)

### Évolutions techniques
- Refactorisation du code du composant treeselect pour permettre l'utilisation de querysets. [#4ddc054](https://github.com/betagouv/seves/pull/4ddc054)
- Amélioration de la sécurité des vues dans le module TIAC. [#52bde16](https://github.com/betagouv/seves/pull/52bde16)
- Utilisation de l'API de rendu de formulaire pour le formulaire Lieu. [#8306378](https://github.com/betagouv/seves/pull/8306378)
- Mise à jour de plusieurs dépendances : `pytest-rerunfailures`, `sentry-sdk`, `ruff`, `django-environ`, `django-debug-toolbar`, `django-reversion`, `redis`, `playwright`.
- Optimisation de la taille des instances Scalingo. [#c6a9665](https://github.com/betagouv/seves/pull/c6a9665)
- Amélioration de la précision des tests dans le module TIAC. [#822bd55](https://github.com/betagouv/seves/pull/822bd55)

### Autres changements
- Correction de plusieurs bugs et améliorations de la stabilité, notamment concernant les modales de conclusion, les dates de publication des notifications, et le comportement des filtres.
- Nettoyage de code et suppression de code mort. [#bedf156](https://github.com/betagouv/seves/pull/bedf156)
- Amélioration des tests unitaires et d'intégration.
- Corrections de typos. [#15945dc](https://github.com/betagouv/seves/pull/15945dc)
- Mise à jour de la configuration de la Content Security Policy (CSP). [#ca1aace](https://github.com/betagouv/seves/pull/ca1aace), [#dc86ad8](https://github.com/betagouv/seves/pull/dc86ad8)
- Exclusion des membres de l'équipe SEVES de la désactivation de compte. [#cb855ac](https://github.com/betagouv/seves/pull/cb855ac)
- Correction du nom de l'en-tête pour TIAC dans les exports CSV. [#2685f87](https://github.com/betagouv/seves/pull/2685f87)
- Ajout d'un message d'information pour l'enregistrement simple lorsque le nombre de personnes malades est supérieur ou égal à 10. [#c7f4e67](https://github.com/betagouv/seves/pull/c7f4e67)
