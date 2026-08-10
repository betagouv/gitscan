## Changelog : anssi-portail (30 derniers jours, au 06/08/2026)

### Résumé
Ce mois a été marqué par une refonte visuelle majeure et une amélioration significative de l'expérience utilisateur, notamment via l'introduction de nouveaux composants graphiques ("Héros riche") et une meilleure gestion du parcours de sécurisation. Le projet a également franchi une étape importante en termes de performance et de référencement grâce à une migration massive vers le rendu côté serveur (SSR).

### Évolutions fonctionnelles
- **Parcours de sécurisation** :
    - Amélioration du suivi de progression avec l'ajout de barres de progression, de badges de complétion et d'indicateurs de mesures par module.
    - Mise en place de tutoriels via des fenêtres modales pour accompagner l'utilisateur.
    - Nouvelle gestion des mesures : affichage sous forme de liste, possibilité d'exporter les mesures au format CSV et ajout de tutoriels dédiés.
- **Récompenses et attestations** :
    - Création d'un générateur de documents pour les attestations (notamment pour le badge Cyberdépart) incluant le nom de l'organisation et respectant la charte graphique (police Marianne).
    - Automatisation de la création d'archives ZIP contenant les badges et les attestations de réussite.
- **Interface et Design (UI/UX)** :
    - Déploiement du nouveau composant "Héros riche" et de nouveaux bandeaux sur l'ensemble des pages (accueil, guides, statistiques, simulateur NIS2, etc.).
    - Amélioration de l'adaptabilité (responsive design) pour les écrans mobiles et tablettes.
    - Ajout d'effets visuels dynamiques, comme l'effet "machine à écrire" sur certains composants.
- **Conformité et suivi** :
    - Mise en place d'un système de gestion du consentement pour le pixel de suivi (tracking).

### Évolutions techniques
- **Performance et SEO** :
    - Migration vers le rendu côté serveur (SSR) pour une large gamme de composants (fil d'Ariane, guides, statistiques, carrousels, pages NIS2, etc.), optimisant ainsi la vitesse de chargement et le référencement.
- **Architecture et Refactoring** :
    - Refactorisation du système de gestion des ressources et des chemins (`fournisseurChemin`).
    - Modularisation et extraction de composants Svelte réutilisables (Tuile, machine à écrire, modales).
    - Standardisation des appels API via une instance `axios` mutualisée et sécurisée.
    - Fusion des entités "entité" et "organisation" pour simplifier le modèle de données.
- **Sécurité et CI/CD** :
    - Renforcement de la sécurité des redirections par une validation systématique côté serveur.
    - Amélioration de la protection des données sensibles (obfuscation et masquage des variables d'environnement).
    - Intégration de scans antivirus dans le pipeline de déploiement (CI).
- **Qualité logicielle** :
    - Augmentation de la couverture de tests avec l'ajout de tests de snapshot pour les composants critiques.

### Autres changements
- **SEO** : Redirection automatique de l'ancienne URL `/guides` vers le nouveau `/catalogue`.
- **Maintenance** : Nettoyage général du code, suppression de commentaires obsolètes et harmonisation de l'arborescence des tests.
