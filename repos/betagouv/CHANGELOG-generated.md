# Synthèse d'activité : betagouv (du 22/04 au 22/05)

## Résumé de l'activité
L'activité récente de l'organisation betagouv se concentre sur l'amélioration de la robustesse, de la sécurité et de la fonctionnalité de ses nombreux projets. Plusieurs dépôts ont bénéficié de mises à jour de dépendances pour corriger des vulnérabilités et améliorer la stabilité. Des efforts importants ont été déployés pour améliorer l'expérience utilisateur, notamment sur les plateformes `mon-service-securise`, `jeveuxaider-front`, `infomedicament` et `mle-front`.  Des fonctionnalités clés ont été ajoutées, comme la gestion du cycle de vie des données dans `euphrosyne` et l'intégration de Matomo dans `mle-back` pour un meilleur suivi des données.  Plusieurs projets ont également vu des améliorations de leur infrastructure et de leur processus de déploiement, comme `metabase-scalingo` et `euphrosyne-tools-infra`.

## Sécurité
Plusieurs dépôts ont bénéficié de mises à jour de sécurité :
- Correction d'une vulnérabilité dans `mon-suivi-justice` avec une mise à jour de la gem `rack-session`.
- Correction d'une vulnérabilité d'injection SQL dans `eva-serveur`.
- Correction d'une faille de sécurité sur TarteauCitronJS dans `eva-serveur`.
- Mises à jour de dépendances dans `infomedicament-dataeng` et `euphrosyne-tools-api` pour corriger des vulnérabilités.

## Autres changements notables
- Refonte de l'architecture de `prestagri` avec la mise en place d'une infrastructure initiale.
- Passage à Poetry pour la gestion des dépendances dans `infomedicament-data`.
- Migration des migrations Drizzle dans `fondation`.
- Refactorisation de la gestion des données dans `euphrosyne` avec l'implémentation d'états "chaud" et "froid".
- Remplacement de Nominatim par geo.api.gouv.fr dans `eva-serveur`.
- Mise à jour de Next.js dans `grist-custom-widgets-fr-admin`.

## Dépôts les plus actifs
- **zacharie:** Ajout de nouvelles fonctionnalités pour la gestion des fiches et des carcasses, amélioration de l'interface utilisateur et implémentation d'un système d'authentification.
- **test-sme:** Amélioration de l'expérience utilisateur avec des refontes de menus, corrections de bugs et mises à jour de l'infrastructure CI/CD.
- **sylvasan:** Ajout de la gestion des brouillons d'enquêtes, nouvelle interface utilisateur et support pour les vocabulaires.
- **stage-direct:** Amélioration de l'authentification, ajout de tests et refonte de la configuration TRPC.
- **mon-service-securise:** Intégration du Design System FR, refonte de la page "Sécuriser" et ajout de la gestion des administrateurs.
- **euphrosyne:** Implémentation de la gestion du cycle de vie des données et améliorations de l'infrastructure.
- **infomedicament:** Ajout de classes cliniques PATHOS, amélioration de la recherche et correction de bugs.
- **mle-front:** Ajout de filtres, amélioration de la carte de mission et ajout de statistiques.
- **fondation:** Ajout de la suppression de sessions de nomination, filtrage des nominations et gestion des pièces jointes.
- **grist-core:** Amélioration de l'importation depuis Airtable, limitation du nombre d'options dans les formulaires et correction de bugs.
