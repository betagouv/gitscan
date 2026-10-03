# Synthèse d'activité : suitenumerique (du 29/04 au 02/10/2026)

## Résumé de l'activité
L'activité récente de la suite est marquée par une montée en puissance des outils de communication et de collaboration, avec l'intégration de la messagerie Matrix dans [hub](/repos/suitenumerique/hub), l'enrichissement des capacités d'IA dans [conversations](/repos/suitenumerique/conversations) et l'amélioration de l'expérience vidéo dans [meet](/repos/suitenumerique/meet). 

Parallèlement, la gestion documentaire et le partage de fichiers gagnent en puissance et en sécurité grâce aux évolutions majeures du moteur de permissions de [drive](/repos/suitenumerique/drive) et à la robustesse accrue des transferts dans [transfers](/repos/suitenumerique/transfers). Ces évolutions visent à offrir une expérience utilisateur plus fluide, tant sur le web que sur mobile, tout en garantissant une souveraineté et une sécurité renforcées.

## Sécurité
- Correction de vulnérabilités critiques (CVE) et mise en place de limitations de débit (throttling) dans [meet](/repos/suitenumerique/meet).
- Protection contre les attaques de type SSRF (Server-Side Request Forgery) lors de l'analyse d'URL dans [file-scanner](/repos/suitenumerique/file-scanner).
- Renforcement des protocoles d'authentification, de déconnexion (OIDC) et respect des standards RFC 9700 dans [accounts](/repos/suitenumerique/accounts) et [django-lasuite](/repos/suitenumerique/django-lasuite).
- Sécurisation des accès via des listes blanches d'adresses IP dans [transfers](/repos/suitenumerique/transfers), [messages](/repos/suitenumerique/messages) et [st-ansible](/repos/suitenumerique/st-ansible).
- Amélioration de la gestion des secrets, du hachage des mots de passe (Argon2) et de l'introspection des jetons dans [menshen](/repos/suitenumerique/menshen).
- Implémentation du protocole PKCE pour sécuriser les connexions dans [drive-migrator](/repos/suitenumerique/drive-migrator).

## Autres changements notables
- **Migrations architecturales et technologiques** : Passage à une structure monorepo pour [ui-kit](/repos/suitenumerique/ui-kit), migration du site de documentation vers Astro pour [docs-website](/repos/suitenumerique/docs-website) et migration du frontend vers Vite pour [calendars](/repos/suitenumerique/calendars).
- **Évolutions de l'infrastructure de stockage** : Adoption de RustFS pour le stockage d'objets local dans [drive](/repos/suitenumerique/drive) et migration vers Garage pour les services média dans [meet](/repos/suitenumerique/meet).
- **Refontes d'interface majeures** : Nouvelle ergonomie mobile pour [messages](/repos/suitenumerique/messages), intégration complète de l'écosystème Matrix pour [hub](/repos/suitenumerique/hub) et refonte du processus de confirmation (RSVP) dans [calendars](/repos/suitenumerique/calendars).

## Dépôts les plus actifs
- [meet](/repos/suitenumerique/meet) : Améliorations majeures de l'expérience de partage d'écran, de l'accessibilité et de la sécurité.
- [drive](/repos/suitenumerique/drive) : Refonte profonde du moteur de permissions et de l'infrastructure de stockage.
- [hub](/repos/suitenumerique/hub) : Intégration complète et riche de la messagerie Matrix (threads, réactions, temps réel).
- [conversations](/repos/suitenumerique/conversations) : Ajout d'outils d'IA avancés (recherche web, génération de présentations) et mise à jour du SDK.
- [ui-kit](/repos/suitenumerique/ui-kit) : Consolidation des composants et transition vers une architecture monorepo.
- [dictaphone](/repos/suitenumerique/dictaphone) : Optimisation du traitement audio et enrichissement de l'expérience mobile.
