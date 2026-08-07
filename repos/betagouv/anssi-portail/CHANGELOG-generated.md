## Changelog : anssi-portail (30 derniers jours, au 06/08/2026)

### Résumé
Ce mois a été marqué par une modernisation majeure de l'interface utilisateur et une amélioration significative de l'expérience de suivi de la cybersécurité. Le déploiement d'un nouveau composant visuel ("Héro") sur l'ensemble du site et l'enrichissement du "Parcours de sécurisation" (avec suivi de progression et génération automatique d'attestations) sont les évolutions les plus notables. Parallèlement, un effort important a été porté sur les performances via le rendu côté serveur (SSR).

### Évolutions fonctionnelles
- **Parcours de sécurisation** :
    - Mise en place d'un suivi de progression détaillé (barres de progression, badges de complétion et compteurs de mesures par module).
    - Ajout de tutoriels interactifs via des modales pour accompagner l'utilisateur.
    - Amélioration de l'affichage des modules (descriptions, ordres d'affichage et vue en liste).
    - Possibilité d'exporter les mesures sous format CSV.
- **Récompenses et attestations** :
    - Automatisation de la génération de documents PDF (attestations Cyberdépart) incluant le nom de l'organisation et respectant la charte graphique (police Marianne).
    - Création d'archives ZIP de récompenses contenant les badges et les attestations.
- **Interface et Design (DA)** :
    - Déploiement du nouveau composant "Héro" (riche et adaptatif) sur la quasi-totalité des pages (accueil, catalogue, statistiques, services, etc.).
    - Nouvelle identité visuelle pour les "Demandes de Diagnostic" avec des éléments graphiques enrichis.
    - Optimisation de l'affichage sur mobile et tablette.
- **Navigation et SEO** :
    - Redirection automatique de l'ancienne route `/guides` vers le `/catalogue`.
    - Amélioration de la navigation via le fil d'Ariane.
- **Conformité et suivi** :
    - Implémentation d'un système de gestion du consentement pour le suivi via pixel (intégration Brevo).

### Évolutions techniques
- **Performance et SEO** :
    - Migration massive de composants vers le rendu côté serveur (SSR) pour améliorer la vitesse de chargement et le référencement (Héro, guides, catalogue, NIS2, etc.).
- **Architecture et Code** :
    - Migration de certains composants vers Svelte 5.
    - Refactorisation de la gestion des appels API via la généralisation d'une instance `axios` sécurisée.
    - Optimisation de la gestion des données avec l'utilisation d'identifiants UUID v7.
    - Unification des définitions de retour d'API et des gestionnaires Express.
- **Sécurité** :
    - Renforcement de la validation des URLs de redirection côté serveur.
    - Obfuscation et masquage des variables d'environnement.
- **Infrastructure et CI/CD** :
    - Ajout d'étapes de scan antivirus dans le pipeline de CI.
    - Introduction de Nix Shell pour faciliter la configuration de l'environnement de développement local.

### Autres changements
- Réorganisation de la documentation (README).
- Nettoyage général du code, des commentaires et des styles CSS inutilisés.
- Amélioration de la couverture de tests (snapshots et tests de composants).
