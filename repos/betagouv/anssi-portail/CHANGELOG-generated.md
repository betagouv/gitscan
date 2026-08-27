## Changelog : anssi-portail (30 derniers jours, au 27 août 2026)

### Résumé
Ce mois a été marqué par une transformation majeure de l'expérience utilisateur avec le déploiement du nouveau "Parcours de sécurisation" et une refonte visuelle globale (nouvelle Direction Artistique). Les utilisateurs bénéficient désormais de fonctionnalités de récompenses enrichies (téléchargement de badges et attestations) et d'une interface plus moderne et animée. Le projet a également bénéficié d'une consolidation technique importante pour soutenir ces évolutions.

### Évolutions fonctionnelles
- **Parcours de sécurisation** : 
    - Mise en place des pages d'atterrissage pour les parcours "complet" et "basique".
    - Nouveau système de récompenses permettant de télécharger une archive ZIP contenant le badge, l'attestation et la bannière de réussite.
    - Amélioration du suivi de l'utilisateur (mémorisation du parcours et de la campagne d'origine).
- **Refonte visuelle (Nouvelle DA)** :
    - Déploiement d'un nouveau design sur l'ensemble du portail : page d'accueil, test de maturité, pages NIS 2, et modules de parcours.
    - Introduction de nouveaux composants visuels tels que le "Héros riche" (avec effets de machine à écrire) et des illustrations animées.
    - Mise à jour des graphiques et des indicateurs de niveau pour le test de maturité.
- **Cyberdépart** : Ajout d'une page dédiée au partage du badge et intégration d'un badge "bêta".
- **Navigation et Ergonomie** :
    - Amélioration du fil d'Ariane pour une meilleure compréhension de la hiérarchie des pages.
    - Optimisation de l'affichage mobile, notamment pour les animations et les textes.
    - Mise à jour de la section "Guides et ressources" sur la page d'accueil.

### Évolutions techniques
- **Pilotage des fonctionnalités** : Implémentation de *feature flags* pour contrôler le déploiement progressif des nouveaux parcours et de la nouvelle identité visuelle.
- **Tracking et Analytics** : Intégration de l'outil Brevo pour le suivi des événements clés (complétion de parcours, déblocage de badges, changements de parcours).
- **Architecture et Backend** :
    - Refonte de la gestion des redirections d'URLs historiques et centralisation des chemins de ressources.
    - Optimisation de l'API de statistiques (satisfaction utilisateur et diagnostics).
    - Amélioration de la robustesse de la gestion des nonces et de la sécurité des en-têtes (rate-limiting).
- **Infrastructure et CI/CD** :
    - Migration de la gestion des paquets vers `pnpm`.
    - Ajout de scans antivirus dans les workflows de CI/CD.
    - Amélioration de la suite de tests (ajout de tests de snapshot pour les documents et bannières).
- **Optimisation des performances** : 
    - Gestion intelligente des animations (lecture uniquement lorsque l'élément est visible à l'écran).
    - Optimisation du chargement des ressources et des composants Svelte.

### Autres changements
- **Nettoyage du code** : Suppression massive de composants Svelte, de styles CSS/SCSS, d'images, de polices et de ressources TypeScript inutilisés.
- **Documentation** : Mise à jour des guides de développement, des procédures d'exploitation et de la documentation de la toolchain.
- **Qualité** : Renforcement des règles de linting et ajout de vérifications automatiques du formatage de code.
