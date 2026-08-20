## Changelog : labonnealternance (30 derniers jours, au 19 août 2026)

### Résumé
Ce mois a été marqué par un tournant majeur avec le déploiement du nouveau moteur de recherche (v2) et une optimisation profonde du référencement naturel (SEO) pour améliorer la visibilité de la plateforme sur Google. Parallèlement, de nouveaux outils d'administration ont été déployés pour faciliter la gestion des partenaires et des CFA, tandis que des automatisations de relance (via Brevo) ont été mises en place pour dynamiser la mise en relation entre candidats et recruteurs.

### Évolutions fonctionnelles
- **Moteur de recherche :** Bascule du moteur de recherche bêta vers la version principale (v2) [#4785] et intégration d'une enquête de satisfaction via Tally [#5056].
- **SEO & Visibilité :** Amélioration massive du référencement via l'ajout de données structurées (Course, ItemList, JobPosting) sur les pages de destination et une meilleure visibilité des résultats de recherche sur Google.
- **Gestion & Administration :** Création d'un écran d'administration pour la gestion des offres partenaires [#5135] et d'une interface dédiée pour les entreprises de type CFA [#4974].
- **Contenu & Accompagnement :** Enrichissement du guide sur la rémunération, mise à jour de la carte des métiers 2026-2027 et ajout de nouveaux articles dans le guide CFA.
- **Engagement utilisateur :** Mise en place de campagnes de relance automatisées pour les candidats inactifs et les entreprises (nurturing) via Brevo.
- **Expérience utilisateur :** Unification de la modale de clôture de recrutement et amélioration de la navigation mobile.

### Évolutions techniques
- **Performance :** Optimisation de la vitesse de navigation grâce à l'adoption de "Cache Components" et du "Partial Prefetching" (Next.js 16.3) pour des transitions quasi instantanées.
- **Intelligence Artificielle :** Migration de la classification des offres partenaires vers le modèle Mistral [#5131].
- **Sécurité :** Implémentation de limitations de débit (rate limiting) sur Nginx pour prévenir le scraping et rotation des clés API Mistral.
- **Architecture & Code :** 
    - Migration vers TypeScript 7, Next.js 16.3 et Biome 2.5.7.
    - Refactoring massif pour passer l'ensemble de la structure de fichiers au format `kebab-case`.
    - Migration vers Zod v4.
- **Fiabilité :** Amélioration de la gestion des erreurs d'API et des processus de recherche (gestion des synonymes et des clauses de repli).

### Autres changements
- **Documentation :** Rédaction des principes d'architecture pour les agents IA [#5125].
- **Maintenance :** Mise à jour de l'image Docker de Metabase et nettoyage de la base de données (backfill de champs manquants).
