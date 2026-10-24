# Synthèse d'activité : suitenumerique (du 16/10 au 23/10/2026)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une montée en puissance des services de communication et de gestion de données. L'intégration majeure de la messagerie Matrix dans [hub](/repos/suitenumerique/hub) et les avancées sur [dictaphone](/repos/suitenumerique/dictaphone) et [conversations](/repos/suitenumerique/conversations) renforcent l'offre collaborative de la suite. Parallèlement, [drive](/repos/suitenumerique/drive) et [transfers](/repos/suitenumerique/transfers) ont bénéficié d'optimisations cruciales pour la gestion de gros volumes et la fiabilité des échanges de fichiers.

L'accent a également été mis sur l'expérience utilisateur et le pilotage, avec de nouveaux outils d'administration dans [st-deploycenter](/repos/suitenumerique/st-deploycenter) et une interface enrichie pour [calendars](/repos/suitenumerique/calendars) et [docs](/repos/suitenumerique/docs). Ces évolutions visent à offrir une plateforme plus robuste, pilotable et accessible pour les utilisateurs finaux et les administrateurs.

## Sécurité
- **Protection contre les attaques réseau** : Renforcement de la sécurité contre les attaques SSRF dans [transfers](/repos/suitenumerique/transfers) et [file-scanner](/repos/suitenumerique/file-scanner).
- **Détection de menaces** : Introduction d'un nouveau moteur de détection de malwares via le protocole ICAP dans [django-lasuite](/repos/suitenumerique/django-lasuite).
- **Confidentialité et protection des données** : Garantie que les prompts utilisateurs ne sont pas enregistrés dans les journaux dans [conversations](/repos/suitenumerique/conversations) et masquage des clés API dans [messages](/repos/suitenumerique/messages).
- **Correction de vulnérabilités** : Résolution de failles critiques (XSS, CVE diverses) dans [projects](/repos/suitenumerique/projects), [meet](/repos/suitenumerique/meet) et [people](/repos/suitenumerique/people).
- **Durcissement de l'authentification** : Adoption de nouveaux algorithmes de hachage (Argon2) et amélioration des flux OIDC dans [menshen](/repos/suitenumerique/menshen) et [accounts](/repos/suitenumerique/accounts).

## Autres changements notables
- **Migrations d'infrastructure** : Passage massif du stockage objet de MinIO vers RustFS ou Silo pour [drive](/repos/suitenumerique/drive), [docs](/repos/suitenumerique/docs) et [accounts](/repos/suitenumerique/accounts).
- **Standardisation du développement** : Lancement du dépôt [ci](/repos/suitenumerique/ci) proposant une bibliothèque de workflows GitHub Actions réutilisables pour l'ensemble de la suite.
- **Modernisation technologique** : Migration du frontend vers Vite pour [calendars](/repos/suitenumerique/calendars) et reconstruction complète du site de documentation avec Astro pour [docs-website](/repos/suitenumerique/docs-website).

## Dépôts les plus actifs
- [drive](/repos/suitenumerique/drive) : Optimisations de performance SQL, nouveaux outils d'administration et mise en place de l'observabilité.
- [meet](/repos/suitenumerique/meet) : Améliorations du partage d'écran, de l'accessibilité et corrections de sécurité majeures.
- [hub](/repos/suitenumerique/hub) : Intégration complète et temps réel de la messagerie Matrix.
- [st-ansible](/repos/suitenumerique/st-ansible) : Introduction de nouveaux services (Conversations, Transfers) et optimisation de l'infrastructure réseau.
- [dictaphone](/repos/suitenumerique/dictaphone) : Améliorations de l'expérience mobile et stabilisation du traitement audio.
- [transfers](/repos/suitenumerique/transfers) : Sécurisation intensive de l'API et amélioration de la fiabilité des téléchargements volumineux.
