## Changelog : anssi-portail (30 derniers jours, au 14 août 2026)

### Résumé
Ce mois-ci, le portail a franchi une étape majeure avec le déploiement des parcours de sécurisation et la génération automatique de récompenses (badges, attestations). L'ensemble de l'interface a été modernisé via une nouvelle direction artistique, et les performances de chargement ont été significativement améliorées grâce à une refonte technique profonde du rendu des pages.

### Évolutions fonctionnelles
- **Parcours de sécurisation** : Mise en place des parcours utilisateurs (basique et complet) avec suivi de progression, attribution de motifs de parcours et gestion des modules.
- **Récompenses et attestations** : Automatisation de la génération de documents (attestations PDF avec police Marianne, badges et archives ZIP) pour les utilisateurs ayant complété leurs parcours.
- **Refonte visuelle (Nouvelle DA)** : Modernisation complète de l'interface avec de nouveaux composants "Héros", une nouvelle palette de couleurs, des illustrations enrichies et l'utilisation systématique des composants du Design System (DSFR).
- **Test de maturité** : Amélioration de l'expérience utilisateur avec un nouveau carrousel des niveaux, des graphiques de résultats mis à jour et de nouvelles illustrations.
- **Navigation et contenu** : Ajout de nouvelles sections sur la page d'accueil (NIS2, "Protéger mon organisation") et mise à jour des rubriques "Guides et ressources".
- **Suivi et consentement** : Implémentation d'un système de suivi (pixel) avec gestion explicite du consentement de l'utilisateur.

### Évolutions techniques
- **Optimisation des performances (SSR)** : Migration massive de composants clés (Héros, fil d'Ariane, carrousels, tuiles, etc.) vers le rendu côté serveur (Server-Side Rendering) pour un affichage plus rapide.
- **Architecture Backend** : Refonte de la gestion des parcours, de la hiérarchie des middlewares et de la validation sécurisée des URLs de redirection.
- **Génération de documents** : Développement d'un moteur de génération de documents et d'archives côté serveur.
- **Sécurité et CI/CD** : Ajout d'étapes de scan antivirus dans la chaîne de production et renforcement du masquage des variables d'environnement.
- **Tests** : Amélioration de la fiabilité via l'ajout de tests de snapshot et une meilleure intégration des outils de test (Vitest, Playwright).

### Autres changements
- **Documentation** : Mise à jour des guides de développement, des procédures d'exploitation et de la documentation de la toolchain.
- **Maintenance du code** : Nettoyage important du projet (suppression de composants et de pages obsolètes, optimisation du CSS et renforcement du typage TypeScript).
