## Changelog : zero-logement-vacant (30 derniers jours, au 28 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'authentification avec une migration vers Better Auth pour une sécurité renforcée, l'ajout de fonctionnalités pour la gestion des documents de campagne, et des corrections de bugs pour améliorer la stabilité et l'expérience utilisateur. Des efforts ont également été faits pour améliorer l'accessibilité et la performance de l'application.

### Évolutions fonctionnelles
- **Gestion des documents de campagne :** Ajout de la possibilité de joindre des documents aux campagnes, avec une interface dédiée pour le téléchargement et la gestion de ces documents. [#1919](https://github.com/MTES-MCT/zero-logement-vacant/pulls/1919)
- **Sauvegarde de campagne :** Possibilité d'enregistrer une campagne à partir d'un groupe existant, avec une interface modale pour la sélection du groupe. [#1918](https://github.com/MTES-MCT/zero-logement-vacant/pulls/1918)
- **Filtre intercommunalité :** Correction du filtre intercommunalité dans la recherche de logements. [#1865](https://github.com/MTES-MCT/zero-logement-vacant/pulls/1865)
- **Amélioration de la cartographie :** Les périmètres sont maintenant affichés en contour et les périmètres inclus restent visibles. [#1884](https://github.com/MTES-MCT/zero-logement-vacant/pulls/1884)

### Évolutions techniques
- **Authentification :** Migration vers Better Auth pour une authentification plus sécurisée et moderne. Cela inclut la gestion des sessions, la synchronisation des utilisateurs et l'amélioration de la sécurité.
- **Compression des réponses API :** Implémentation de la compression des réponses API pour améliorer les performances. [#1925](https://github.com/MTES-MCT/zero-logement-vacant/pulls/1925)
- **Refactoring :** Refactorisation du code pour améliorer la maintenabilité et la lisibilité.
- **Tests :** Ajout et amélioration des tests unitaires et d'intégration, notamment pour l'authentification et les nouvelles fonctionnalités.
- **Outils de réparation :** Développement d'un outil en ligne de commande (CLI) pour effectuer des réparations sur la base de données.
- **Infrastructure :** Amélioration de la configuration de l'infrastructure, notamment pour la gestion de la base de données.
- **RGAA :** Amélioration de l'accessibilité de l'application pour se conformer aux normes RGAA.

### Autres changements
- **Documentation :** Mise à jour de la documentation pour refléter les changements apportés à l'application.
- **Corrections de bugs :** Correction de divers bugs mineurs pour améliorer la stabilité et l'expérience utilisateur.
- **Mises à jour de dépendances :** Mise à jour de certaines dépendances pour bénéficier des dernières corrections de bugs et améliorations de sécurité.
- **Amélioration des messages d'erreur :** Clarification des messages d'erreur pour faciliter le débogage.
- **Amélioration des logs :** Ajout de logs plus informatifs pour faciliter le suivi des événements.
- **Correction de l'étiquette énergétique dans l'export :** Correction de l'utilisation de la bonne colonne pour l'étiquette énergétique lors de l'export des données. [#1818](https://github.com/MTES-MCT/zero-logement-vacant/pulls/1818)
- **Correction des utilisateurs LOVAC Cerema :** Déduplication des utilisateurs LOVAC Cerema par adresse e-mail. [#1888](https://github.com/MTES-MCT/zero-logement-vacant/pulls/1888)
