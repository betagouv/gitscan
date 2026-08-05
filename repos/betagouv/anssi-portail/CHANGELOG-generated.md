## Changelog : anssi-portail (30 derniers jours, au 04 août 2026)

### Résumé
Ce mois-ci, le portail a franchi des étapes majeures avec le déploiement des parcours de sécurisation, incluant désormais un suivi de progression détaillé et un système de récompenses (badges et attestations). L'expérience utilisateur a été transformée par une refonte visuelle (nouveau composant "Héros") et une amélioration significative de la fluidité grâce à la généralisation du rendu côté serveur (SSR).

### Évolutions fonctionnelles
- **Parcours de sécurisation :**
    - Mise en place d'un suivi de progression complet (barres de progression, badges de complétion et indicateurs de mesures réalisées par module).
    - Introduction de tutoriels interactifs via des fenêtres modales pour accompagner l'utilisateur dans ses démarches.
    - Nouveau système de récompenses permettant de télécharger des archives ZIP contenant des badges et des attestations officielles (PDF) personnalisées.
    - Ajout de la possibilité d'exporter les mesures de sécurité au format CSV.
- **Interface et Design :**
    - Refonte visuelle de la page d'accueil et des pages clés avec un nouveau composant "Héros" (Hero) enrichi, incluant des animations (effet machine à écrire) et une meilleure adaptabilité sur mobile et tablette.
    - Déploiement de nouveaux éléments graphiques (bandeaux riches, décorations visuelles) pour améliorer l'ergonomie.
- **Confidentialité :**
    - Mise en place d'un système de gestion du consentement pour le suivi utilisateur (pixel de suivi).

### Évolutions techniques
- **Performance et SEO :**
    - Migration massive vers le rendu côté serveur (SSR) pour de nombreux composants critiques (catalogue, guides, fil d'Ariane, tableaux NIS2, etc.), optimisant la vitesse de chargement et le référencement naturel.
    - Optimisation de la gestion des redirections d'URL et des liens canoniques.
- **Sécurité et CI/CD :**
    - Renforcement de la sécurité de la chaîne de déploiement avec l'ajout de scans antivirus et de la validation de configuration (`zizmor`).
    - Durcissement de la gestion des secrets et des identifiants dans les workflows GitHub.
- **Architecture :**
    - Refactorisation importante des composants de l'UI Kit (Tuile, Lien, etc.) pour une meilleure réutilisation.
    - Passage à l'utilisation des UUID v7 pour la génération des clés primaires.
    - Amélioration de la robustesse de la récupération des statistiques et de la gestion des erreurs.

### Autres changements
- **Développement :** Introduction de Nix Shell pour simplifier la configuration de l'environnement de développement local.
- **Documentation :** Réorganisation du fichier README.
- **Maintenance :** Nettoyage général du code, suppression de styles CSS obsolètes et harmonisation de la structure des tests.
