## Changelog : anssi-portail (30 derniers jours, au 21 août 2026)

### Résumé
Ce mois a été marqué par une refonte visuelle majeure du portail via l'application d'une nouvelle charte graphique (Design System) sur l'ensemble des pages. Le projet a également franchi une étape importante dans l'automatisation des parcours de sécurisation, notamment avec la génération automatique de récompenses (badges et attestations en PDF/ZIP) et l'amélioration de l'interactivité grâce à de nouvelles illustrations animées.

### Évolutions fonctionnelles
- **Refonte visuelle globale** : Application de la nouvelle direction artistique sur l'ensemble du portail (Accueil, pages NIS2, Collectivités, Associations, Entreprises, Test de maturité, etc.) avec l'utilisation de nouveaux composants et motifs de fond.
- **Enrichissement des parcours de sécurisation** : 
    - Création de nouvelles pages d'atterrissage (*landing pages*) pour les parcours "Basique" et "Complet".
    - Mise en place de tutoriels interactifs via des fenêtres modales.
    - Automatisation des récompenses : génération d'archives ZIP et de documents PDF (attestations, badges) incluant le nom de l'organisation et respectant la typographie officielle.
- **Amélioration du Test de maturité** : Refonte complète de l'interface de test et de l'affichage des résultats (nouveaux graphiques, couleurs et composants DSFR).
- **Expérience utilisateur et interactivité** :
    - Intégration d'illustrations animées (marelle, dragon, etc.) et d'effets visuels (machine à écrire).
    - Amélioration de la navigation grâce à l'ajout et l'unification du fil d'Ariane.
    - Optimisation de l'affichage mobile et correction de divers problèmes de mise en page (menus, boutons, images).
- **Corrections de contenu** : Mise à jour des termes non officiels (ex: remplacement de "CyFun23"), correction des textes (wording) et des informations de contact.

### Évolutions techniques
- **Refactorisation de l'architecture** :
    - Réécriture de l'intégration Brevo pour utiliser une architecture par classes et un système piloté par les événements.
    - Isolation de l'état d'exécution de Serena et amélioration de la gestion des middlewares.
- **Sécurité et fiabilité** :
    - Renforcement de la gestion des nonces et de la validation des URLs de redirection côté serveur.
    - Implémentation du hachage des emails pour les communications via Brevo.
    - Amélioration du suivi (*tracking*) des événements et des parcours utilisateurs.
- **Expérience de développement (DX) et CI/CD** :
    - Support du développement en réseau local (LAN).
    - Mise à jour de la chaîne d'outils : Vite, Express, TypeScript, pnpm et ESLint.
    - Optimisation de la CI/CD avec l'ajout de scans antivirus et de vérifications de formatage.
    - Intégration d'outils d'IA pour le développement (configuration pour Claude/Codex et compétences d'intégration Figma).

### Autres changements
- **Documentation** : Réorganisation du guide de développement et mise à jour de la documentation technique (toolchain, procédures d'exploitation).
- **Nettoyage** : Suppression de pages obsolètes (ex: pages "promouvoir"), de dépendances inutilisées et de styles CSS redondants.
