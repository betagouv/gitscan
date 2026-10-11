## Changelog : les-emplois (30 derniers jours, au 10 octobre 2026)

### Résumé
Ce mois a été marqué par une transformation majeure de l'identité visuelle de la plateforme, désormais nommée "La plateforme de l'inclusion". Les évolutions se sont concentrées sur l'automatisation et la fluidification du parcours d'orientation (insertion), l'enrichissement du profil des usagers avec une nouvelle vue d'ensemble, et le renforcement de la traçabilité grâce à la mise en place d'un système d'audit.

### Évolutions fonctionnelles

**Parcours d'orientation (Insertion)**
- Refonte complète de l'expérience utilisateur pour les orientations : nouveau wizard, pages de détails des orientations et des structures.
- Automatisation du suivi : expiration automatique des orientations et envoi de notifications par email (création, acceptation, refus, rappels automatiques aux structures).
- Amélioration des fonctionnalités pour les prestataires : possibilité d'accepter ou de refuser une orientation avec saisie de motifs détaillés.
- Gestion simplifiée des accès via des liens magiques (magic links) permettant une consultation anonyme des détails de l'orientation.

**Profil Usager**
- Création d'un nouvel onglet "Vue d'ensemble" (expérimental) regroupant les informations clés : conseillers référents, état des contrats et dernières candidatures.
- Amélioration de la gestion des affectations avec l'ajout de filtres et d'une icône d'archivage pour les anciennes affectations.
- Ajout d'alertes contextuelles (ex: opportunités d'immersion, fin de contrat proche).
- Mise à jour de la terminologie : généralisation du terme "Usager" en remplacement de "Candidat".

**Gestion des dossiers employés**
- Refonte du workflow de gestion des dossiers : nouveaux états, transitions améliorées et gestion dynamique des badges de statut.
- Amélioration de la visibilité dans l'interface d'administration (suivi des mises à jour des données surveillées).

**Accès et Sécurité**
- Généralisation de l'usage de ProConnect : l'authentification devient obligatoire pour tous les professionnels et institutionnels.
- Amélioration du processus d'activation et de récupération de compte pour les professionnels.

**Interface et Marque**
- Changement de branding : nouveau nom ("La plateforme de l'inclusion"), nouveaux logos et mise à jour de l'identité visuelle sur l'ensemble du site.
- Harmonisation de l'interface (icônes des organisations, mise en page des formulaires d'extension d'approbation).

### Évolutions techniques

**Traçabilité et Audit**
- Implémentation d'un système d'audit (audit trail) pour suivre les actions critiques et les informations de navigation (browser, IP).

**Performance et Optimisation**
- Optimisation du temps de démarrage du service (gain de 600ms en évitant la résolution d'URL au setup).
- Amélioration des performances via l'utilisation de méthodes de queryset optimisées et la mise en cache des clés de sécurité (JWKS).

**Communications**
- Modernisation des emails : passage au format Markdown pour le corps des messages et ajout d'alternatives texte/HTML pour une meilleure délivrabilité.

**Infrastructure et Qualité**
- Amélioration de la CI/CD, notamment pour le déploiement des "review apps".
- Renforcement de la qualité du code via des corrections de typage (mypy) et une meilleure gestion des tests (mocking, isolation des scopes Sentry).

### Autres changements
- Nettoyage important du code : suppression des dépendances et des commandes liées à l'ancien système DORA.
- Mise à jour de la documentation technique et des pages légales/accessibilité pour refléter le nouveau branding.
- Refactorisation de plusieurs composants utilitaires et gestion des fichiers de configuration.
