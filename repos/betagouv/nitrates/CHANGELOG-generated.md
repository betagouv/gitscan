## Changelog : nitrates (30 derniers jours, au 31 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment sur mobile, avec une refonte du formulaire de couvert végétal et une meilleure gestion des dates. Des corrections de sécurité importantes ont également été implémentées, ainsi qu'une amélioration de l'infrastructure CI/CD et des outils d'administration.

### Évolutions fonctionnelles
- **Formulaire couvert végétal :** Refonte complète du formulaire pour une meilleure expérience utilisateur, notamment sur mobile, avec des dates plus accessibles et une navigation simplifiée [#272].
- **Calendrier :** Amélioration du récapitulatif du calendrier avec des sections plus claires et des justifications plus précises [#159].
- **Simulation :** Possibilité de relancer une simulation après avoir modifié des paramètres [#175].
- **Cartographie :** Correction de bugs et améliorations de l'affichage de la carte [#271, #193].
- **Administration :** Ajout d'un filtre rapide pour les conditions dans l'interface d'administration et amélioration de la recherche et de l'édition des textes conditionnés [#222, #218, #219].
- **Validation :** Amélioration de l'interface de validation avec un comparateur d'images et un panel de détails en auto-save.
- **Ouverture géographique :** Application correcte de l'ouverture géographique sur la page publique.

### Évolutions techniques
- **Sécurité :** Correction de plusieurs vulnérabilités de sécurité, notamment une faille XSS et des problèmes liés à l'authentification admin [#150, #197].
- **CI/CD :** Mise en place d'une infrastructure CI/CD plus robuste avec des workflows GitOps et des tests automatisés [#50].
- **Infrastructure :** Amélioration de la gestion des dépendances et des environnements de déploiement.
- **Tests :** Adaptation des tests pour couvrir les nouvelles fonctionnalités et les modifications apportées.
- **Refactoring :** Refactorisation du code pour améliorer la maintenabilité et la performance.
- **Gestion des données :** Normalisation des données et amélioration de la gestion des référentiels.

### Autres changements
- **Documentation :** Mise à jour de la documentation pour refléter les changements apportés.
- **Contenus :** Mise à jour des textes et des libellés pour une meilleure clarté et une meilleure cohérence [#160].
- **Accessibilité :** Amélioration de l'accessibilité du simulateur au clavier [#247].
- **Dark Mode :** Corrections d'affichage en mode sombre [#189].
- **Divers :** Corrections de bugs mineurs et améliorations diverses de l'interface utilisateur.
